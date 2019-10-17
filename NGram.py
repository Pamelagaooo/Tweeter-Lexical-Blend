import pygtrie
import textdistance
import numpy
import editdistance
import pygtrie as trie
import ngram
import math
import sys

updated_cad_list = list()
updated_candidates = open("updated_candidates.txt", "r")
if updated_candidates.mode == "r":
    handler_c = updated_candidates.readlines()
    for x in handler_c:
        y = x.split()
        updated_cad_list.append(y[0])

dictionary1 = open("dict.txt", "r")
if dictionary1.mode == "r":
    handler_d = dictionary1.readlines()

# create a dictionary structure for dict.txt
dictionary_list = list()
new_dictionary = dict()
for x in handler_d:
    y = x.split()
    dictionary_list.append(y[0])
for word in dictionary_list:
    character = word[:1]
    if not character in new_dictionary:
        new_dictionary[character] = list()
    new_dictionary[character].append(word)

prefix_word_list = list()
current = 0
for word in updated_cad_list:
    current += 1
    sys.stdout.write("\r | complete: {}, total: {}".format(current, len(updated_cad_list)))

    total_length = len(word)
    length = math.floor(total_length/2)
    prew = word[:length]

    for vocal in new_dictionary[word[0]]:
        prev = vocal[:length]
        pre_distance = ngram.NGram.compare(prew, prev, N = 2)
        if (word not in prefix_word_list) and (pre_distance >= 0.5):
            prefix_word_list.append(word)

match = open("ngram_pre.txt", "w")
if match.mode == "w":
    for item in prefix_word_list:
        match.write("%s\n" % item)
