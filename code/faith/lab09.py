import math
import os

books = os.path.join(os.getcwd('lab09.txt'))
# print('The book: ', books)
result = ""
for files in os.listdir(books):
    # print('files', files)
    if files.endswith('.txt'):
        file = files.split('.')
        with open(os.path.join(books, files), 'r') as f:
            read_files = f.read()


            num_sent = 0
            for x in read_files:
                if x in['.','?','!']:
                    num_sent += 1


            words = read_files.split()
            print('The Type: ',type(words))
            num_words = len(words)


            num_letters = 0
            for word in words:
                print('word', word)

            num_letters += len(word)



            ARI = 4.71 * (num_letters/num_words) + 0.5 *(num_words/num_sent)-21.43
            print(num_letters, num_words)
            ARI = math.ceil(ARI)
            if ARI > 14:
                ARI = 14
            print('text', num_letters, num_words, num_sent )
            ari_scale = {
                1: {'ages':   '5-6', 'grade': 'Kindergarten'},
                2: {'ages':   '6-7', 'grade':    '1st Grade'},
                3: {'ages':   '7-8', 'grade':    '2nd Grade'},
                4: {'ages':   '8-9', 'grade':    '3rd Grade'},
                5: {'ages':  '9-10', 'grade':    '4th Grade'},
                6: {'ages': '10-11', 'grade':    '5th Grade'},
                7: {'ages': '11-12', 'grade':    '6th Grade'},
                8: {'ages': '12-13', 'grade':    '7th Grade'},
                9: {'ages': '13-14', 'grade':    '8th Grade'},
                10: {'ages': '14-15', 'grade':    '9th Grade'},
                11: {'ages': '15-16', 'grade':   '10th Grade'},
                12: {'ages': '16-17', 'grade':   '11th Grade'},
                13: {'ages': '17-18', 'grade':   '12th Grade'},
                14: {'ages': '18-22', 'grade':      'College'}
            }


            grade = ari_scale[ARI]
            result = f"The ARI for {file} is {ARI} "
            result += f"This corresponds to a {grade['grade']} level of difficulty"
            result += f"\n that is suitable for an average person {grade['ages']} years old\n"
print(result) 



