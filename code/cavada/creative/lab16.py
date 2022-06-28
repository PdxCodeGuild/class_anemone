from creative.pyble import bible
import pprint

text = bible.get_chapter()
# print(text)

import sys

sys.stdout = open("dump.txt","w", encoding= 'utf-8')
print(text)
sys.stdout.close()
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
