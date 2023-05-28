import os

path = 'test_file_2.txt'

if os.path.isfile(path):
    os.remove(path)