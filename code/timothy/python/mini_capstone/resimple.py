import os
import time
from playsound import playsound
import reprlib

# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples

class resimple():
    def __init__(self):
        self.filepath = input("Enter path to sample directory: ")

    def display_folders(self):
        folders_in_path = os.listdir(self.filepath)
        print(f'Sample directory includes these folders: {folders_in_path}')
        choose_folder = input("Choose folder to enter: ")
        if choose_folder in folders_in_path:
            samps_in_folder = os.listdir(self.filepath + '/' + choose_folder)
        pre_full = input('See (P)review or (F)ull list of files? ').lower()
        if pre_full == 'f':
            print('\n'.join(samps_in_folder))
        elif pre_full == 'p':                                                       # reprlib allows for limits on list and string prints
            r = reprlib.Repr()
            r.maxlist = 4
            r.maxstring = 20
            print(r.repr(samps_in_folder))
        return samps_in_folder

    def sample_player(self): 
        repr(samps_in_folder)
        samples = os.listdir(samps_in_folder)
        for sample in samples:
            print(sample)
            playsound(sample)
            stop_play = input("Press Enter for next sample or type Stop: ").lower()
            if stop_play == 'stop':
                break
        print(f'End of samples...')



def main():

    print('Welcome to reSimple - Renaming samples, simply.')

    user = resimple()

    resimple.display_folders(user)


    while True:
        command = input("\n[Return] to Parent Folder\n[Play] Samples in Folder\n[Batch] Rename Folder Contents\n").lower()
        if command == 'return':
            resimple.display_folders(user)
        elif command == 'play':
            resimple.sample_player(user)


main()

