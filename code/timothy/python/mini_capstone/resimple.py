import os
import time
from playsound import playsound
import reprlib
from pathlib import Path
import librosa

# C:/Users/johns/pdx_code_guild/class_anemone/code/timothy/python/mini_capstone/samples

class resimple():
    def __init__(self):
        self.filepath = input("Enter path to sample directory: ")


    def display_folders(self):
        folders_in_path = os.listdir(self.filepath)
        print(f'Sample directory includes these folders: {folders_in_path}')
        while True:
            choose_folder = input("Choose folder to enter: ")
            if choose_folder in folders_in_path:
                samps_in_folder = os.listdir(self.filepath + '/' + choose_folder)
                break
            else:
                print(f'Folder not in sample directory...\nPlease choose from {folders_in_path}: ')            
        pre_full = input('See (P)review or (F)ull list of files? ').lower()
        if pre_full == 'f':
            print('\n'.join(samps_in_folder))
        elif pre_full == 'p':                                                       # reprlib allows for limits on list and string prints
            r = reprlib.Repr()
            r.maxlist = 4
            r.maxstring = 20
            print(r.repr(samps_in_folder))
        samples = self.filepath + '/' + choose_folder
        return samples

    # def play_sound(self, sample):
    #     playsound(sample)
    #     return

    def sample_player(self, samples):
        repr(samples)
        sample = os.listdir(samples)
        for i in range(len(sample)):
            print(sample[i])
            wav = os.path.join(samples, sample[i])
            playsound(wav)
            # playsound.close()
            name_check = input("Press Enter to play next sample, or type Stop: ").lower()
            if name_check == 'stop':
                break
        

    def batch_rename(self, samples):
            i = 0
            batch_name = input('New Batch Sample Name: ').title()
            for filename in os.listdir(samples):
                # print(samples)
                # print(filename)
                new_name = batch_name + '(' + str(i) + ')' + '.wav'
                if new_name in samples:
                    break
                else: os.rename(os.path.join(samples, filename), os.path.join(samples, new_name))
                i+=1     
            print(f"Sample batch renamed {batch_name}().wav")


# user = resimple()
# # resimple.display_folders(user)
# resimple.sample_player(user)

def main():

    print('Welcome to reSimple - Renaming samples, simply.')
    time.sleep(2)
    user = resimple()
    originldir = os.getcwd()
    sample_path = resimple.display_folders(user)
    samples = Path(sample_path)
    os.chdir(samples)
    

    while True:
        command = input("\n[Return] to Parent Folder\n[Play] Samples in Folder\n[Batch] Rename Folder Contents\n\n").lower()
        if command == 'return':
            sample_path = resimple.display_folders(user)
            samples = Path(sample_path)
            os.chdir(samples)
        elif command == 'play':
            resimple.sample_player(user, samples)
            os.chdir(originldir)
        elif command == 'batch':
            resimple.batch_rename(user, sample_path)


main()

