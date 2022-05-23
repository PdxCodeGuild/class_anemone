import pprint
pyble = {
    1: {
        '1 chronicles': {},
        '1 kings': {},
        '1 samuel': {},
        '2 chronicles': {},
        '2 kings': {},
        '2 samuel': {},
        'amos': {},
        'daniel': {},
        'deuteronomy': {},
        'ecclesiastes': {},
        'esther': {},
        'exodus': {},
        'ezekiel': {},
        'ezra': {},
        'genesis': {},
        'habukkuk': {},
        'haggai': {},
        'hosea': {},
        'isaiah': {},
        'jeremiah': {},
        'job': {},
        'joel': {},
        'jonah': {},
        'joshua': {},
        'judges': {},
        'lamentations': {},
        'leviticus': {},
        'malachi': {},
        'micah': {},
        'nahum': {},
        'nehemiah': {},
        'numbers': {},
        'obadiah': {},
        'proverbs': {},
        'psalms': {},
        'ruth': {},
        'song of solomon': {},
        'zechariah': {},
        'zephaniah': {}
        },
    2: {
        '1 corinthians': {},
        '1 john': {},
        '1 peter': {},
        '1 thessalonians': {},
        '1 timothy': {},
        '2 corinthians': {},
        '2 john': {},
        '2 peter': {},
        '2 thessalonians': {},
        '2 timothy': {},
        '3 john': {},
        'acts': {},
        'colossians': {},
        'ephesians': {},
        'galatians': {},
        'hebrews': {},
        'james': {},
        'john': {},
        'jude': {},
        'luke': {},
        'mark': {},
        'matthew': {},
        'philemon': {},
        'philippians': {},
        'revelation': {},
        'romans': {},
        'titus': {}
    }
}

o_dict_list = [{'book1':'chapters'},{'book2': 'chapters'},{'book3': 'chatpers'}]
n_dict_list = [{'book1':'chapters'},{'book2': 'chapters'},{'book3': 'chatpers'}]



pyble = [{'old testament':o_dict_list},{'new testament':n_dict_list}]
# pprint.pprint(pyble)
print((pyble[0]['old testament']))
