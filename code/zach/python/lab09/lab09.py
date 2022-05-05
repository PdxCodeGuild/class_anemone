from data import *
import re
import math


def ari_calc(text_file):
    filename = open(text_file)
    text_data = filename.read()
    chars = len(re.findall('( *?[0-9a-zA-Z] *?)', text_data))
    words = len(text_data.split())
    sentences = len(re.split('[.?!]', text_data))-1

    ari_eq = math.floor(4.71*(chars/words) + 0.5*(words/sentences)-21.43)
    return ari_eq


def main():
    text_input = 'gettysburg_address.txt'
    ari_score = ari_calc(text_input)
    # ari_scale[ari_calc(text_input)]
    reccomended_age = ari_scale[ari_score]['ages']
    reccomended_grade = ari_scale[ari_score]['grade_level']


    print(f'The ARI for { text_input } is { ari_score } This corresponds to a { reccomended_grade} Grade level of difficulty that is suitable for an average person { reccomended_age } years old.')


if __name__ == '__main__':
    main()
