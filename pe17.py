p= {'1-9': ['one',
         'two',
         'three',
         'four',
         'five',
         'six',
         'seven',
         'eight',
         'nine'],
 '10-19': ['ten',
           'eleven',
           'twelve',
           'thirteen',
           'fourteen',
           'fifteen',
           'sixteen',
           'seventeen',
           'eighteen',
           'nineteen'],
 '20-90': ['twenty',
           'thirty',
           'forty',
           'fifty',
           'sixty',
           'seventy',
           'eighty',
           'ninety'],
 'x00': 'hundred'}


def hundred(num):
    pfx = 0
    le = 0
    if num > 0:
        pfx = len(p['1-9'][num - 1]) + len(p['x00'])
        le += pfx
        pfx += 3 #and 
        le += pfx * 99
    le += sum([len(x) for x in p['1-9']])
    le += sum([len(x) for x in p['10-19']])
    le += sum([len(x) + sum([len(y) + len(x) for y in p['1-9']]) for x in p['20-90']])
    return le


print(sum([hundred(x) for x in range(0, 10)]) + 11)#11 one thousand