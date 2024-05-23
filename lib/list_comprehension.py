#!/usr/bin/env python3

def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]

num_list = [0, 1, 3, 5, 7, 8, 9]
even_numbers = return_evens(num_list)
print(even_numbers)



def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    return [sentence + '!' for sentence in sentence_list]

sentence_list = ["Hello", "I'm doing great", "Python is fun"]
exclamation_list = make_exclamation(sentence_list)
print(exclamation_list)

    
