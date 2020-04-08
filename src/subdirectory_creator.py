#!/usr/bin/env python

import os

path = os.getcwd()
print("Current path: %s" % path)
check = input("Do you want to continue in this directory? y/n ")
if check in ['y', 'Y', 'yes', 'Yes', 'YES']:
    name = input("Insert main folder name: ")
    dirName = path + "/" + name
    os.mkdir(dirName)
    value = input("How many subfolders do you want to create? ")
    i = 1
    while i<= value:
        number = str(i)
        completeDir = dirName + "/new_folder " + number
        os.mkdir(completeDir)
        i = i + 1
else:
    print("Move subdirectory_creator.py to the desired location")

