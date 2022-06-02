import random
import string


class Paw2():
    def __init__(self):
        self.letters=[]
        self.numbers=[]
        self.characters=[]
        self.letter = string.ascii_letters
        self.number = string.digits
        self.special_charc = string.punctuation
        
    def gen(self, let, num, char):
        self.letters.clear()
        self.numbers.clear()
        self.characters.clear()
        
        for x in range(let):
            str(self.letters.append(random.choice(self.letter)))
        for x in range(num):
            str(self.numbers.append(random.choice(self.number)))
        for x in range(char):
            str(self.characters.append(random.choice(self.special_charc)))
        
        password = self.letters + self.numbers + self.characters
        random.shuffle(password)
        password = (''.join(password))
        
        return password
    
    





