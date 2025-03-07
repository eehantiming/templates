""" 
Reads through files in a directory (it must not contain nested dirs)
Identify the duplicate files e.g. IMG_8888.JPG; IMG_8888 (1).JPG
Delete/ Move them to another dir.

0. Install requirements
1. put this script with the dir to cleanup. Update FILE_DIR and EXT_TYPES
2. python3 main.py
3. A new dir duplicated/ will be created inside FILE_DIR with the duplicates.
"""

import os 
import shutil
import cv2
import numpy as np
from tqdm import tqdm

FILE_DIR = "test"
NEW_DIR = os.path.join(FILE_DIR,"duplicates") # test/duplicates
EXT_TYPES = ["JPG", "MOV", "png"]
all_files = os.listdir(FILE_DIR)

indexes_of_duplicate = []

for i, filename in enumerate(tqdm(all_files)): # IMG_8888 (1).JPG
    filename_wo_ext, ext = filename.split('.') # IMG_8888 (1)
    assert ext in EXT_TYPES
    # Check if file is a potential duplicate from name
    filename_list = filename_wo_ext.split('(')
    if len(filename.split('(')) == 1:
        continue
    root_filename = f"{filename_list[0].strip()}.{ext}" # IMG_8888.JPG
    if root_filename in all_files:
        # Check if videos are identical by comparing first frame
        if ext == "MOV":
            cap1 = cv2.VideoCapture(os.path.join(FILE_DIR,filename))
            cap2 = cv2.VideoCapture(os.path.join(FILE_DIR,root_filename))
            _,image1 = cap1.read()
            _,image2 = cap2.read()
            cap1.release()
            cap2.release()
        else:
            image1 = cv2.imread(os.path.join(FILE_DIR,filename))
            image2 = cv2.imread(os.path.join(FILE_DIR,root_filename))
        # Check if the pixels are identical    
        if image1.shape == image2.shape and not (np.bitwise_xor(image1,image2).any()):
            # print(f"{filename}, {root_filename} SAME IMAGE!")
            indexes_of_duplicate.append(i)
        # else:
            # print(f"{filename}, {root_filename} DIFF IMAGE!")

# Move the marked files to a new directory
if not os.path.exists(NEW_DIR):
    os.makedirs(NEW_DIR)            

for i in tqdm(indexes_of_duplicate):
    filename = os.path.join(FILE_DIR,all_files[i]) # test/IMG_8888 (1).jpg
    # os.remove(filename)
    shutil.move(filename, NEW_DIR)
print(f"{len(indexes_of_duplicate)} duplicates.")
