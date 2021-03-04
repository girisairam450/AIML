# # Creating Train / Val / Test folders
import os
import numpy as np
import shutil
import random
root_dir = 'D:/POC Projects/Tata Steel - Defect Detection/black_patch_generated_frames/sample_images_' # data root path

val_ratio = 0.15
test_ratio = 0.05

# for cls in classes_dir:
os.makedirs(root_dir +'train/')
os.makedirs(root_dir +'val/')
os.makedirs(root_dir +'test/')


# Creating partitions of the data after shuffeling
src = 'D:/POC Projects/Tata Steel - Defect Detection/black_patch_generated_frames/sample_images'

allFileNames = os.listdir(src)
np.random.shuffle(allFileNames)
train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)* (1 - (val_ratio + test_ratio))), 
                                                           int(len(allFileNames)* (1 - test_ratio))])


train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Validation: ', len(val_FileNames))
print('Testing: ', len(test_FileNames))

# Copy-pasting images
for name in train_FileNames:
    shutil.copy(name, root_dir +'train/')

for name in val_FileNames:
    shutil.copy(name, root_dir +'val/')

for name in test_FileNames:
    shutil.copy(name, root_dir +'test/')