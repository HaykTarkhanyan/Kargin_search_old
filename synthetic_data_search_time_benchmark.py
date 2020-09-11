import pandas as pd
import numpy as np
import string
import random
# data = pd.read_csv('Ցավդ տանեմ ընգերներով միհատ search engine ենք ուզում կառուցենք, միհատ վիդյոի տեքստ չի հերիքում, ցավդ տանեմ (3).xlsx')

# print (data.head())
# a = pd.DataFrame()


# def get_random_alphanumeric_string(length):
#     letters_and_digits = string.ascii_letters + string.digits 
#     result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
#     # print("Random alphanumeric String is:", result_str)
#     return result_str


# def generate_random_sentence(num_words, length):
#     sentence = [get_random_alphanumeric_string(random.randint(5, 15)) for i in range(num_words)]

#     return ' '.join(sentence)

# # print (generate_random_sentence(4))

# a['names'] = [generate_random_sentence(random.randint(10, 60), random.randint(5,12)) for i in range(10_000)]

# print (a)
# a.to_csv('sythetic_data_big.csv')
    


# a['names'] = np.zeros((1000))
# print (letters)
# print (a)

import time
from difflib import *

data = pd.read_csv('sythetic_data_big.csv') 
#  3800 kb anoc faela, mer himivan@ 40 a voch anhrajesht sruner@ het@

start = time.time()
strr = 'leudvig'
num_iter = 1_000

# for i in range(num_iter):
#     rand_ind = random.randint(0, len(data))
#     data.loc[rand_ind] = strr

#     a = data[data.names == strr]
#     # data.loc[rand_ind] = 

# print (a)
data.loc[8000] = strr


# print (f'average time {((time.time() - start)) / num_iter}')
st = time.time()
for i in range(num_iter):
    # if i % 50 == 0:
    # print (i)  
    v = get_close_matches('leuda ', data.names, cutoff=0.1)#[0]
    # print (v)
print (f'average time {((time.time() - start)) / num_iter}')


# # def wuzzyfuzzy(df1, strr):
# #     myList = []

# #     possibilities = strr
# #     total = len(df1)

#     s = SequenceMatcher(isjunk=None, autojunk=False)

#     for idx1, df1_str in enumerate(df1.names):
#         my_str = ('Progress : ' + str(round((idx1/total)*100,3))+'%')
#         # sys.stdout.write('\r' + str(my_str))
#         # sys.stdout.flush()

#         # get 1 best match that has a ratio of at least 0.7
#         best_match = get_close_matches(df1_str, possibilities, 1, 0.7)

#         s.set_seq(df1_str, best_match) 
#         myList.append([df1_str, best_match, s.ratio()])

#         return myList

# # print (wuzzyfuzzy(data, strr))