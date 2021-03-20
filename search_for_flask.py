from fuzzywuzzy import process
from fuzzywuzzy import fuzz

import pandas as pd


def do_all(QUERY, NUM_TO_SHOW):
    data = pd.read_csv('kargin_data_first_playlist_unifinished.csv')
    # data = pd.read_csv(PATH)
    print ('starting search')

    # tags = data['Tag'].dropna().tolist()  
    high = data['Phrase, Priority High'].dropna().tolist()
    low = data['Phrase, Priority Normal'].dropna().tolist()

    results = process.extract(QUERY, high + low, limit=NUM_TO_SHOW, scorer=fuzz.partial_ratio)
    print ('got results')

    links = []
    for i in results:
#     print ('link: ')
        if i[0] in high:
            print(data[data['Phrase, Priority High'] == i[0]].links.values[0])
            links.append(data[data['Phrase, Priority High'] == i[0]].links.values[0])
        else:
            print(data[data['Phrase, Priority Normal'] == i[0]].links.values[0])
            links.append(data[data['Phrase, Priority Normal'] == i[0]].links.values[0])

    # if results[0][0] in high:
    #     print (data[data['Phrase, Priority High'] == results[0][0]].links.values[0])
    #     link = data[data['Phrase, Priority High'] == results[0][0]].links.values[0]
        
    # else:
    #     print (data[data['Phrase, Priority Normal'] == results[0][0]].links.values[0])
    #     link = data[data['Phrase, Priority High'] == results[0][0]].links.values[0]
    print ('done')
    return links#s[32:43]
    # return QUERY * 3