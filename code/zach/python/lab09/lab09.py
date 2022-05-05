from fileinput import filename
from data import *
import re
import math


def ari_calc():
    text_file = open('gettysburg_address.txt')
    text_data = text_file.read()
    chars = len(re.findall('( *?[0-9a-zA-Z] *?)', text_data))
    words = len(text_data.split())
    sentences = len(re.split('[.?!]',text_data))-1 

    ari_eq = math.floor(4.71*(chars/words) + 0.5*(words/sentences)-21.43)
    return ari_eq

def main():
    ari_calc()


if __name__ == '__main__':
    main()