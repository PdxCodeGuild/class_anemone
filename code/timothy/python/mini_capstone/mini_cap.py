# ....Function Playground for Mini Capstone Project ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# imports necessary ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
import os
from os import listdir
from pathlib import Path
from posixpath import dirname
from playsound import playsound
from librosa import core
from librosa import beat
import time

# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/snares
# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/breaks

# class/funcs ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

class reSimple:
    def __init__(self):
        pass

    def folder_path(self):
        self.filepath = input("Please enter the path to your sample folder: ")
        return self.filepath

    def folder_contents(self):
        basepath = self.filepath
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                print(entry)
    
    def sample_run(self):
        repr(self.filepath)
        samples = listdir(self.filepath)
        for sample in samples:
            print(sample)
            playsound(self.filepath + '/' + sample)
            next_sound = input("1. Edit \n2. Next Sample\n3. Exit\n").lower()
            if next_sound == '2':
                continue
            elif next_sound == '3':
                break
            elif next_sound == '1':
                return sample
            else: print("Invalid Response")

    def batch_rename(self):
        i = 0
        batch_name = input('New Batch Sample Name: ').lower()
        for filename in os.listdir(self.filepath):
            new_name = batch_name + str(i) + '.wav'
            os.rename(os.path.join(self.filepath, filename), os.path.join(self.filepath, new_name))
            i+=1
        print(f"Samples batch renamed {batch_name}().wav")

tim = reSimple()
reSimple.folder_path(tim)
reSimple.folder_contents(tim)
# reSimple.sample_run(tim)
# reSimple.batch_rename(tim)

