import random
import string
from .models import Urlshort


class Paw2():
    def __init__(self):
        self.letters=[]
        self.numbers=[]
        self.characters=[]
        self.letter = string.ascii_letters
        self.number = string.digits
        self.special_charc = string.punctuation
        
    def gen(self):
        self.letters.clear()
        self.numbers.clear()
        self.characters.clear()
        
        for x in random.choice(0,15):
            str(self.letters.append(random.choice(self.letter)))
        for x in random.choice(0.15):
            str(self.numbers.append(random.choice(self.number)))
        for x in random.choice(0, 18):
            str(self.characters.append(random.choice(self.special_charc)))
        
        url = self.letters + self.numbers + self.characters
        random.shuffle(url)
        surl = (''.join(url))
        
        return surl

    def redo(self, surl):
        if surl in Urlshort.surl:
            Paw2.gen()
        else:
            return surl