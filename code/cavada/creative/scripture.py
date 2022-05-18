import biblia
import time
import random

old_t = ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', '1 samuel', '2 samuel', '1 kings', '2 kings', '1 chronicles', '2 chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'song of solomon', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel','hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habukkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi']
new_t = ['matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1 corinthians', '2 corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1 thessalonians', '2 thessalonians', '1 timothy', '2 timothy', 'titus', 'philemon', 'hebrews', 'james', '1 peter', '2 peter', '1 john', '2 john', '3 john', 'jude', 'revelation']

for testament in bible:

    for book in testament:
        bk = random.choice(old_t)
        if book == bk:
            text = book['text']
            for t in text:
                print(t)
                time.sleep(.1)

