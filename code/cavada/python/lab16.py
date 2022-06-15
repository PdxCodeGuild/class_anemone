import creative.pyble as pyble
pyble = Pyble()
cont = ''
while True and not cont in ['no','n', 'exit', 'quit', 'e','done']:
    command= input("""
    Pyble Reader:
        -(s)earch for passages by phrase or keyword:
        -(r)ead a passage:
    
    """)
    if command=='s':
        pyble.phrase()
    elif command=='r':
        pyble.read()
    else:
        cont=input("cont? ")
        if cont in ['no','n', 'exit', 'quit', 'e','done']:
            break


        """this is a """
# bibby =  [[{
#             'ot': [{
#                 'b1': {
#                     1: {1: 'verse',2: 'verse',3: 'verse'},
#                     2: {1: 'verse',2: 'verse',3: 'verse'},
#                     3: {1: 'verse',2: 'verse',3: 'verse'}
#                     },
#                 'b1': {
#                     1: {1: 'verse',2: 'verse',3: 'verse'},
#                     2: {1: 'verse',2: 'verse',3: 'verse'},
#                     3: {1: 'verse',2: 'verse',3: 'verse'}
#                     },
#                 'b1': {
#                     1: {1: 'verse',2: 'verse',3: 'verse'},
#                     2: {1: 'verse',2: 'verse',3: 'verse'},
#                     3: {1: 'verse',2: 'verse',3: 'verse'}
#                     }]},
#             'nt': [{
#                 'b1': {
#                     1: {1: 'verse',2: 'verse',3: 'verse'},
#                     2: {1: 'verse',2: 'verse',3: 'verse'},
#                     3: {1: 'verse',2: 'verse',3: 'verse'}
#                     },
#                 'b1': {
#                     1: {1: 'verse',2: 'verse',3: 'verse'},
#                     2: {1: 'verse',2: 'verse',3: 'verse'},
#                     3: {1: 'verse',2: 'verse',3: 'verse'}
#                     },
#                 'b1': {
#                     1: {1: 'verse',2: 'verse',3: 'verse'},
#                     2: {1: 'verse',2: 'verse',3: 'verse'},
#                     3: {1: 'verse',2: 'verse',3: 'verse'}
#                     }]
#             }]]


"""this code was used to count words,
 might used this in future for readibility 
 index attribution to verse/chapter/book 
 portions"""
                            # print(f"""number of chapters cum: {n} 
                            # running word ct: {wrd_ct}
                            # running chapter ct: {chap_num}
                            # word ct for last chapter: {last_chap_ct} 
                            #     -num of verses: {i}
                            #     -num of chapters in book: {len(chs)} 
                            # verses in current book cum: {v}
                            # """)

"""phrase examples
-afraid of god
-son of man
-righteous path

demo
show code
tell about dev process
twilio.rest
from twilio.net import client

import smtplib
import scheduler

"""
