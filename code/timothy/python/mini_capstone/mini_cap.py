# ....Function Playground for Mini Capstone Project ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# Necessary Imports
import os
from playsound import playsound
import librosa
from librosa import core
from librosa import beat
import time

# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/snares
# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/breaks

# reSimple - Renaming samples, simply.

class Context_Manager():
    pass

class reSimple:
    def __init__(self):
        self.filepath = input("Please enter the path to your sample folder: ")
        os.chdir(self.filepath)
    
    # def nav_into(self, subfolders):
    #     forward = ('Which folder would you like to work in? ')
    #     if forward in

    def folder_contents(self): # NEEDS NATURAL SORTING
        basepath = self.filepath
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                print(entry)

    # def sample_player(self): #WinError 32 (file is being used), 'with open' somewhere?
    # repr(self.filepath)
    # samples = os.listdir(self.filepath)
    # for sample in samples:
    #     print(sample)
    #     self.play_sound(sample)
    #     name_check = input("Do you need to rename this sample? Y/N ").lower()
    #     if name_check == 'y':
    #         self.sample_rename(sample)
    #         pass
    # print(f'End of samples...')

    def sample_rename(self, sample):
        new_sample_name = input('Rename Sample: ').title()
        new_name = new_sample_name + '.wav'
        old_name = sample
        os.rename(os.path.join(self.filepath, old_name), os.path.join(self.filepath, new_name))
        print(f'Sample renamed {new_name}')
        # return sample

    def play_sound(self, sample):
        playsound(sample)
        return

    
    def sample_player(self): #WinError 32 (file is being used), 'with open' somewhere?
        repr(self.filepath)
        samples = os.listdir(self.filepath)
        for i in range(len(samples)):
            print(samples[i])
            self.play_sound(samples[i])
            while True:
                name_check = input("'R'ename or 'H'ear again?' ").lower()
                if name_check == 'r':
                    self.sample_rename(samples[i])
                    print('yo')
                    continue
                elif name_check == "h":
                    print('hey')
                    break
        print(f'End of samples...')

    def batch_rename(self): # WORKING
            i = 0
            batch_name = input('New Batch Sample Name: ').title()
            for filename in os.listdir(self.filepath):
                new_name = batch_name + '(' + str(i) + ')' + '.wav'
                if new_name in self.filepath:
                    break
                else: os.rename(os.path.join(self.filepath, filename), os.path.join(self.filepath, new_name))
                i+=1     
            print(f"Sample batch renamed {batch_name}().wav")


    def tempo_finder(self): # Runtime Error Opening & FileNotFound Errno 2
        repr(self.filepath)
        samples = os.listdir(self.filepath)
        for sample in samples:
            print(sample)
            # playsound(self.filepath + '/' + sample)
            y, sr = librosa.load(sample)
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            print('Estimated tempo: {:.2f}'.format(tempo))

tim = reSimple()

# reSimple.folder_path(tim) OBSOLETE
# reSimple.folder_contents(tim)
reSimple.sample_player(tim)
# reSimple.batch_rename(tim)
# reSimple.tempo_finder(tim)
















# def main():

#     print('Welcome to reSimple - Renaming samples, simply.')
#     time.sleep(3)
#     user = reSimple()

#     while True:
#         pass
        

# main()