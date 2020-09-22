# բարև, ձեզ բոռդո գույնի ներկ պետքա, դե run կոճակը սխմեք ու 17րդ տողում գրեք ձեր նախադասությունը, ու եթե չկարողանա գտնի սքրինշոթ արեք ու ուղարկեք էլի, 
# Առաջին անգամ օգտագործելուց միքիչ երկար կսպասեք, լավագույն վարկածը ամենավերևումա տպելու

from fuzzywuzzy import process
from fuzzywuzzy import fuzz

import pandas as pd
# import Levenshtein

PATH = 'Ցավդ տանեմ ընգերներով միհատ search engine ենք ուզում կառուցենք, միհատ վիդյոի տեքստ չի հերիքում, ցավդ տանեմ - kargin_titles_links_first_200 (3).csv'
NUM_TO_SHOW = 5

data = pd.read_csv(PATH)

tags = data['Tag'].dropna().tolist()  
high = data['Phrase, Priority High'].dropna().tolist()
low = data['Phrase, Priority Normal'].dropna().tolist()

QUERY = 'ափսոս մերդ մեր հետ չի'
QUERY = 'բայց դե ոնց-որ ես իրանել եմ կրակել'


results = process.extract(QUERY, high + low, limit=NUM_TO_SHOW, scorer=fuzz.partial_ratio)

print ('//' * 15)
print ('**' * 10)
print ('Լավագույն վարկածը'  )
print ('link: ')
if results[0][0] in high:
    print (data[data['Phrase, Priority High'] == results[0][0]].links.values[0])
else:
    print (data[data['Phrase, Priority Normal'] == results[0][0]].links.values[0])
print (print (results[0][0]))
print ('**' * 10)
print ('//' * 15)
print ()

print ('hajord tarberakner@')

for i in results:
    print ('link: ')
    if i[0] in high:
        print (data[data['Phrase, Priority High'] == i[0]].links.values[0])
    else:
        print (data[data['Phrase, Priority Normal'] == i[0]].links.values[0])
    print (i[0])
    print (f'Confidence - {i[1]}')
    print ('**' * 10)
    print ()


# եթե վերևինը սխալ աշխատեց 53 ու 74 տողերի """ ջնջեք ու նորից փորձեք
"""
all_tags = [
    k.strip() for j in [high, low] for i in j
    for k in i.split(".") if k.strip()
]
results = process.extract(QUERY, high + low, limit=10, scorer=fuzz.partial_ratio)

for i in results:
    print (i)
    print ()

print ('errord pordz')
res = process.extract(QUERY, high + low, limit=10, scorer=fuzz.partial_token_set_ratio)
for i in res:
    print (i)
    print ()

print ('chorord pordz')
res = process.extract(QUERY, high + low, limit=10, scorer=fuzz.partial_token_sort_ratio)

for i in res:
    print (i)
    print ()

"""
