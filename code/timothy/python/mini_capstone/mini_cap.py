# ....Function Playground for Mini Capstone Project ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

# Necessary Imports
import os
from more_itertools import sample
from playsound import playsound
import librosa
from librosa import core
from librosa import beat
import time
import reprlib
import pyaudio
import wave
from array import array
from struct import pack

# def play(file):
#     CHUNK = 1024
#     wf = wave.open(file, 'rb')
#     p=pyaudio.PyAudio()
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                         channels=wf.getnchannels(),
#                         rate = wf.getframerate(),
#                         output = True)
#     data = wf.readframes(CHUNK)
#     while len(data)>0:
#         stream.write(data)
#         data = wf.readframes(CHUNK)

#     stream.stop_stream()
#     stream.close
#     p.terminate

# play('C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/snares/Snare(0).wav')

# # C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/snares
# # C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples/breaks

# # reSimple - Renaming samples, simply.

# class Context_Manager():
#     pass

# class reSimple:
#     def __init__(self):
#         self.filepath = input("Please enter the path to your sample folder: ")
#         os.chdir(self.filepath)
    
#     # def nav_into(self, subfolders):
#     #     forward = ('Which folder would you like to work in? ')
#     #     if forward in

#     def folder_contents(self): # NEEDS NATURAL SORTING
#         basepath = self.filepath
#         for entry in os.listdir(basepath):
#             if os.path.isfile(os.path.join(basepath, entry)):
#                 print(entry)

#     # def sample_player(self): #WinError 32 (file is being used), 'with open' somewhere?
#     # repr(self.filepath)
#     # samples = os.listdir(self.filepath)
#     # for sample in samples:
#     #     print(sample)
#     #     self.play_sound(sample)
#     #     name_check = input("Do you need to rename this sample? Y/N ").lower()
#     #     if name_check == 'y':
#     #         self.sample_rename(sample)
#     #         pass
#     # print(f'End of samples...')

#     def sample_rename(self, sample):
#         new_sample_name = input('Rename Sample: ').title()
#         new_name = new_sample_name + '.wav'
#         old_name = sample
#         os.rename(os.path.join(self.filepath, old_name), os.path.join(self.filepath, new_name))
#         print(f'Sample renamed {new_name}')
#         # return sample

#     def play_sound(self, sample):
#         playsound(sample)
#         return

    
#     def sample_player(self): #WinError 32 (file is being used), 'with open' somewhere?
#         repr(self.filepath)
#         samples = os.listdir(self.filepath)
#         for i in range(len(samples)):
#             print(samples[i])
#             self.play_sound(samples[i])
#             while True:
#                 name_check = input("'R'ename or 'H'ear again?' ").lower()
#                 if name_check == 'r':
#                     self.sample_rename(samples[i])
#                     print('yo')
#                     continue
#                 elif name_check == "h":
#                     print('hey')
#                     break
#         print(f'End of samples...')

#     def batch_rename(self): # WORKING
#             i = 0
#             batch_name = input('New Batch Sample Name: ').title()
#             for filename in os.listdir(self.filepath):
#                 new_name = batch_name + '(' + str(i) + ')' + '.wav'
#                 if new_name in self.filepath:
#                     break
#                 else: os.rename(os.path.join(self.filepath, filename), os.path.join(self.filepath, new_name))
#                 i+=1     
#             print(f"Sample batch renamed {batch_name}().wav")


#     def tempo_finder(self): # Runtime Error Opening & FileNotFound Errno 2
#         repr(self.filepath)
#         samples = os.listdir(self.filepath)
#         for sample in samples:
#             print(sample)
#             # playsound(self.filepath + '/' + sample)
#             y, sr = librosa.load(sample)
#             tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#             print('Estimated tempo: {:.2f}'.format(tempo))

# tim = reSimple()

# reSimple.folder_path(tim) OBSOLETE
# reSimple.folder_contents(tim)
# reSimple.sample_player(tim)
# reSimple.batch_rename(tim)
# reSimple.tempo_finder(tim)

















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

    def play(self, file):
        CHUNK = 1024
        wf = wave.open(file, 'rb')
        p=pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate = wf.getframerate(),
                            output = True)
        data = wf.readframes(CHUNK)
        while len(data)>0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close
        p.terminate

    def play_samples(self):
        for i in range(len(self.samples)):
            while True:
                print(self.samples[i])
                self.play(self.folder + '/' + self.samples[i])
                repextop = input('(R)eplay, (N)ext, (S)top ').lower()
                if repextop == 'r':
                    continue
                elif repextop == 'n':
                    break
                elif repextop == 's':
                    return False
        self.samples = os.listdir(self.folder)

    
    def rename_samples(self):
        i = 0
        batch_name = input("Enter batch-name for samples: ").title()
        for file in self.samples:
            new_name = batch_name + '(' + str(i) + ')' + '.wav'
            if new_name == file:
                pass
            else: os.rename(os.path.join(self.folder, file), os.path.join(self.folder, new_name))
            i += 1
        print(f'Samples renamed to {batch_name}().wav')
        self.samples = os.listdir(self.folder)

def main():

    print('\t- ReSimple -\n   Renaming samples, simply!')

    open = resimple()

    while True:

        print("Type the associated number of the action you would like to perform:")
        command = input("\n1. Display samples\n2. Play samples\n3. Rename samples\n4. Switch folders\n5. Quit\n")
        if command == '1':
            open.display_samples()
        elif command == '2':
            open.play_samples()
        elif command == '3':
            open.rename_samples()
        elif command == '4':
            open.switch_folders()
        elif command == '5':
            print('\nThank you for using ReSimple!')
            return False
        else: print('\nThat option does not exist. Type the associated number of the action you would like to perform: ')

main()


# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples