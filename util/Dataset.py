import os
import shutil

class Dataset(object):

    def __init__(self, path):
        self.dogs_path = 'dataset3/Dog'
        self.cats_path = 'dataset3/Cat'

        self.real_data = path

        self.train_dir = os.path.join(self.real_data, 'train')
        self.cat_train_dir = os.path.join(self.train_dir, 'cat')
        self.dog_train_dir = os.path.join(self.train_dir, 'dog')

        self.test_dir = os.path.join(self.real_data, 'test')
        self.cat_test_dir = os.path.join(self.test_dir, 'cat')
        self.dog_test_dir = os.path.join(self.test_dir, 'dog')

        self.valid_dir = os.path.join(self.real_data, 'valid')
        self.cat_valid_dir = os.path.join(self.valid_dir, 'cat')
        self.dog_valid_dir = os.path.join(self.valid_dir, 'dog')
    
    def create_folders(self):
        os.mkdir(self.real_data)
        os.mkdir(self.train_dir)
        os.mkdir(self.cat_train_dir)
        os.mkdir(self.dog_train_dir)
        os.mkdir(self.test_dir)
        os.mkdir(self.cat_test_dir)
        os.mkdir(self.dog_test_dir)
        os.mkdir(self.valid_dir)
        os.mkdir(self.cat_valid_dir)
        os.mkdir(self.dog_valid_dir)

    def create_train_test_valid(self):
        train_list_cat_file = [f'{i}.jpg' for i in range(10000)]
        train_list_dog_file = [f'{i}.jpg' for i in range(10000)]

        test_list_cat_file = [f'{i}.jpg' for i in range(10000, 11250)]
        test_list_dog_file = [f'{i}.jpg' for i in range(10000, 11250)]

        val_list_cat_file = [f'{i}.jpg' for i in range(11250, 12500)]
        val_list_dog_file = [f'{i}.jpg' for i in range(11250, 12500)]

        for filename in train_list_cat_file:
            src = os.path.join(self.cats_path, filename)
            dst = os.path.join(self.cat_train_dir, filename)
            shutil.copyfile(src, dst)
            
        for filename in train_list_dog_file:
            src = os.path.join(self.dogs_path, filename)
            dst = os.path.join(self.dog_train_dir, filename)
            shutil.copyfile(src, dst)

        for filename in test_list_cat_file:
            src = os.path.join(self.cats_path, filename)
            dst = os.path.join(self.cat_test_dir, filename)
            shutil.copyfile(src, dst)
            
        for filename in test_list_dog_file:
            src = os.path.join(self.dogs_path, filename)
            dst = os.path.join(self.dog_test_dir, filename)
            shutil.copyfile(src, dst)
            
        for filename in val_list_cat_file:
            src = os.path.join(self.cats_path, filename)
            dst = os.path.join(self.cat_valid_dir, filename)
            shutil.copyfile(src, dst)
            
        for filename in val_list_dog_file:
            src = os.path.join(self.dogs_path, filename)
            dst = os.path.join(self.dog_valid_dir, filename)
            shutil.copyfile(src, dst)

    def create_dataset(self):
        if not(os.path.exists(self.real_data)):
            self.create_folders()
            self.create_train_test_valid()