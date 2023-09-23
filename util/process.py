import os

#TODO
# Filter the images in dataset2/train/train to folder Cat and folder Dog to improve model performance

"""
path = "dataset3/Dog"
count = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path, filename), os.path.join(path, "{}".format(count)+".jpg"))
    count += 1"""


path = "processed-data/realdata2/valid/dog"
path2 = "processed-data/realdata3/valid/dog"

for i in range(11250, 12500):
    os.rename(os.path.join(path, "{}".format(i)+".jpg"), os.path.join(path2, "{}".format(i+1250)+".jpg"))