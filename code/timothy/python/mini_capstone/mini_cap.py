# ....Function Playground for Mini Capstone Project ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# Necessary Imports
import os
from playsound import playsound
import librosa
from librosa import core
from librosa import beat


# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/snares
# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/breaks

# reSimple - Renaming samples, simply.

class reSimple:
    def __init__(self):
        self.filepath = input("Please enter the path to your sample folder: ")

    # def folder_path(self):
    #     self.filepath = input("Please enter the path to your sample folder: ")
    #     return self.filepath

    def folder_contents(self): # NEEDS NATURAL SORTING
        basepath = self.filepath
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                print(entry)

    def sample_rename(self, sample):
        new_sample_name = input('Rename Sample: ').lower()
        new_name = new_sample_name + '.wav'
        os.rename(os.path.join(self.filepath, sample), os.path.join(self.filepath, new_name))
        print(f'Sample renamed {new_name}')
        return sample
    
    def sample_player(self): #WinError 32 (file is being used), 'with open' somewhere? or split off new function for 'rename' to call within.
        repr(self.filepath)
        samples = os.listdir(self.filepath)
        for sample in samples:
            print(sample)
            playsound(self.filepath + '/' + sample)
            name_check = input("Do you need to rename this sample? Y/N ").lower()
            if name_check == 'y':
                self.sample_rename(sample)
        print(f'End of samples...')

    def batch_rename(self): # WORKING
            i = 0
            batch_name = input('New Batch Sample Name: ').title()
            for filename in os.listdir(self.filepath):
                new_name = batch_name + '(' + str(i) + ')' + '.wav'
                os.rename(os.path.join(self.filepath, filename), os.path.join(self.filepath, new_name))
                i+=1     
            print(f"Samples batch renamed {batch_name}().wav")


    def tempo_finder(self): # Runtime Error Opening & FileNotFound Errno 2
        repr(self.filepath)
        samples = os.listdir(self.filepath)
        for sample in samples:
            print(sample)
            playsound(self.filepath + '/' + sample)
            y, sr = librosa.load(sample)
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

tim = reSimple()

# reSimple.folder_path(tim) OBSOLETE
# reSimple.folder_contents(tim)
# reSimple.sample_player(tim)
reSimple.batch_rename(tim)
# reSimple.tempo_finder(tim)
