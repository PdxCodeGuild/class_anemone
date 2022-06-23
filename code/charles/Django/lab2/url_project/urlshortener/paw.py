import random
import string
from .models import Urlshort


class Paw2():
    def __init__(self):
        self.letters=[]
        self.numbers=[]
        
        self.letter = string.ascii_letters
        self.number = string.digits
        
        
    def gen(self):
        self.letters.clear()
        self.numbers.clear()
        
        
        for x in range(0, 5):
            str(self.letters.append(random.choice(self.letter)))
        for x in range(0, 5):
            str(self.numbers.append(random.choice(self.number)))
        
        
        url = self.letters + self.numbers 
        random.shuffle(url)
        pawurl = (''.join(url))
        
        return pawurl

    def redo(self, pawurl):
        surls= Urlshort.objects.all()
        if pawurl in surls:
            Paw2.gen()
        else:
            return pawurl