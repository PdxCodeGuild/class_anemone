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

tim = reSimple()
reSimple.folder_path(tim)
# reSimple.folder_contents(tim)
reSimple.sample_run(tim)

