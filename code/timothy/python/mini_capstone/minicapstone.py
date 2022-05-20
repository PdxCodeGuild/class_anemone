import os
import time
import reprlib
from pathlib import Path
from playsound import playsound

# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples

class resimple():
    def __init__(self):
        self.filepath = input("Enter path to sample directory: ")
        self.folders = os.listdir(self.filepath)
        print(f'Sample directory includes these folders: {self.folders}')
        while True:
            choose_folder = input("Choose folder to enter: ")
            if choose_folder in self.folders:
                samples = os.listdir(self.filepath + '/' + choose_folder)
                folder = self.filepath + '/' + choose_folder
                break
            else:
                print(f'Folder not in sample directory...\nPlease choose from {self.folders}: ')
            # return samples
        self.samples = samples
        self.folder = folder
        self.og_dir = os.getcwd()
        self.newdir = os.chdir(self.filepath + '/' + choose_folder)
        

    def switch_folders(self):
        print(f'Sample directory includes these folders: {self.folders}')
        while True:
            choose_folder = input("Choose folder to enter: ")
            if choose_folder in self.folders:
                samples = os.listdir(self.filepath + '/' + choose_folder)
                folder = self.filepath + '/' + choose_folder
                break
            else:
                print(f'Folder not in sample directory...\nPlease choose from {self.folders}: ')            
        self.samples = samples
        self.folder = folder
        self.og_dir = os.getcwd()
        self.newdir = os.chdir(self.filepath + '/' + choose_folder)
        
    def display_samples(self):
        pre_full = input('See (P)review or (F)ull list of files? ').lower()
        if pre_full == 'f':
            print('\n'.join(self.samples))
        elif pre_full == 'p':
            r = reprlib.Repr()
            r.maxlist = 4
            r.maxstring = 20
            print(r.repr(self.samples))

    def play_samples(self):
        for i in range(len(self.samples)):
            print(self.samples[i])
            playsound(self.folder + '/' + self.samples[i])
            # repextop = input('(R)eplay, (N)ext, (S)top ').lower()
            
        
def main():

    print('\t- ReSimple -\n   Renaming samples, simply!')

    open = resimple()

    while True:

        print("Type the associated number of the action you would like to perform:")
        command = input("1. Display samples\n2. Play samples\n3. Rename samples\n4. Switch folders\n5. Quit\n")
        if command == '1':
            open.display_samples()
        elif command == '2':
            open.play_samples()
        elif command == '4':
            open.switch_folders()

main()