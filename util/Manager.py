import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import platform

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import cv2

from keras.layers import Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator 

def resizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

class Manager(object):

    def __init__(self, dataset):
        plt.rc('font', size=24)
        self.dataset = dataset
        self.create_image_generators()
        self.create_model()

    def create_image_generators(self):
        train_gen = ImageDataGenerator(rescale=1./255)
        validation_gen = ImageDataGenerator(rescale=1./255.)
        test_gen = ImageDataGenerator(rescale=1./255.)

        self.class_names = ["cat", "dog"]

        self.train_generator = train_gen.flow_from_directory(
            self.dataset.train_dir,
            target_size=(150, 150),
            batch_size=64,
            class_mode='binary')

        self.validation_generator = validation_gen.flow_from_directory(
            self.dataset.valid_dir,
            target_size=(150, 150),
            batch_size=64,
            class_mode='binary')

        self.test_generator = test_gen.flow_from_directory(
            self.dataset.test_dir,
            target_size=(150, 150),
            batch_size=64,
            class_mode='binary')

    def create_model(self):
        inputs = tf.keras.layers.Input(shape=(150,150,3))
        x =  tf.keras.layers.Conv2D(32, (3,3), activation='relu')(inputs)
        x = tf.keras.layers.Conv2D(64, (3,3), activation='relu')(x)
        x = tf.keras.layers.MaxPooling2D(2,2)(x)

        x = tf.keras.layers.Conv2D(64, (3,3), activation='relu')(x)
        x = tf.keras.layers.Conv2D(128, (3,3), activation='relu')(x)
        x = tf.keras.layers.MaxPooling2D(2,2)(x)

        x = tf.keras.layers.Conv2D(128, (3,3), activation='relu')(x)
        x = tf.keras.layers.Conv2D(256, (3,3), activation='relu')(x)
        x = tf.keras.layers.GlobalAveragePooling2D()(x)
        x = Dense(1024,activation='relu')(x)
        x = tf.keras.layers.Dense(2, activation='softmax')(x) 

        self.model = Model(inputs=inputs, outputs=x)

        if platform.processor == "arm":
            self.optimizer = tf.keras.optimizers.legacy.RMSprop(learning_rate=0.001)
        else:
            self.optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)

        self.model.compile(optimizer=self.optimizer,
                    loss='sparse_categorical_crossentropy',
                    metrics = ['accuracy'])
    
    def load(self, path):
        path = path + '/weights'
        self.model.load_weights(path).expect_partial()

    def save(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            path = path + '/weights'
            self.model.save_weights(path)

    def train(self, epochs):
        _ = self.model.fit(self.train_generator, epochs=epochs, validation_data=self.validation_generator)

    def evaluate(self):
        _, acc = self.model.evaluate(self.test_generator, verbose=2)
        print("Restored model, accuracy: {:5.2f}%".format(100 * acc))
    
    def predict(self, image_path):
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        img_to_show = cv2.imread(image_path)
        img_to_show = resizeWithAspectRatio(img_to_show, width=600)

        img_to_show = cv2.putText(img_to_show, "{} / {:.2f}%".format(self.class_names[np.argmax(score)], 100 * np.max(score)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Image", img_to_show)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()