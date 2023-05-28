# os.listdir() method

import os

path = '../dataset'
all_files = os.listdir(path)

for files in all_files:
    if os.path.isfile(os.path.join(path, files)):
        print("{} is a file".format(files))


# os.scandir() method

all_files = os.scandir(path)

for file in all_files:
    if file.is_file():
        print("{} is a file".format(file.name))

# using pathlib module
import pathlib

# path object construct

path_object = pathlib.Path(path)

for file in path_object.iterdir():
    if file.is_file():
        print(file.name)