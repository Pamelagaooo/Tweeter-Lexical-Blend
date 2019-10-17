import pygtrie
import textdistance
import numpy
import editdistance
import pygtrie as trie
import NGram
import math
import sys

#prefix part
dictionary1 = open("dict.txt", "r")
if dictionary1.mode == "r":
    handler_d = dictionary1.readlines()

true_blend_list = list()
true_blend = open("blends.txt", "r")
if true_blend.mode == "r":
    handler_t = true_blend.readlines()
    for x in handler_t:
        y = x.split()
        true_blend_list.append(y[0])
print(true_blend_list)

updated_cad_list = list()
updated_candidates = open("updated_candidates.txt", "r")
if updated_candidates.mode == "r":
    handler_c = updated_candidates.readlines()
    for x in handler_c:
        y = x.split()
        updated_cad_list.append(y[0])

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

# create a reverse dictionary structure for dict.txt

dictionary_list_r = list()
new_dictionary_r = dict()
for x in handler_d:
    y = x.split()
    dictionary_list_r.append(str((y[0])[::-1]))

for term in dictionary_list_r:
    character = term[0]
    if character not in new_dictionary_r:
        new_dictionary_r[character] = list()
    new_dictionary_r[character].append(term)


#calculate Jaro-winkler similarity between candidates and dictionary word (prefix)
prefix_list = list()
current = 0
for cad in updated_cad_list:
    current += 1
    sys.stdout.write("\r | complete: {}, total: {}".format(current, len(updated_cad_list)))
    char = cad[:1]
    for vocal in new_dictionary[char]:
        sim = textdistance.jaro_winkler.similarity(cad, vocal)
        if (sim>= 0.8) and (cad not in prefix_list):
            prefix_list.append(cad)

match = open("jaro_pre.txt", "w")
if match.mode == "w":
    for item in prefix_list:
        match.write("%s\n" % item)

#suffix part

import pygtrie
import textdistance
import numpy
import editdistance
import math
import sys

dictionary1 = open("dict.txt", "r")
if dictionary1.mode == "r":
    handler_d = dictionary1.readlines()


dictionary_list_r = list()
new_dictionary_r = dict()
for x in handler_d:
    y = x.split()
    z = str((y[0])[::-1])
    dictionary_list_r.append(z)

for term in dictionary_list_r:
    character = term[0]
    if character not in new_dictionary_r:
        new_dictionary_r[character] = list()
    new_dictionary_r[character].append(term)

true_blend_list = list()
true_blend = open("blends.txt", "r")
if true_blend.mode == "r":
    handler_t = true_blend.readlines()
    for x in handler_t:
        y = x.split()
        true_blend_list.append(y[0])

post_list = list()
post = open("jaro_post.txt", "r")
if post.mode == "r":
    handler_t = post.readlines()
    for x in handler_t:
        y = x.split()
        post_list.append(str((y[0])[::-1]))


matched_list = list()
for term in post_list:
    if term in true_blend_list:
        matched_list.append(term)

length2 = len(matched_list)
print(length2)

match = open("match_Jaro.txt", "w")
if match.mode == "w":
    for item in matched_list:
        match.write("%s\n" % item)

prefix_list = list()
prefixes = open("jaro_pre.txt", "r")
if prefixes.mode == "r":
    handler_p = prefixes.readlines()
    for x in handler_p:
        y = x.split()
        z = str((y[0])[::-1])
        prefix_list.append(z)

#

postfix_list = list()
current = 0
for cad in prefix_list:
    current += 1
    sys.stdout.write("\r | complete: {}, total: {}".format(current, len(prefix_list)))
    char = cad[:1]
    for vocal in new_dictionary_r[char]:
        sim = textdistance.jaro_winkler.similarity(cad,vocal)
        if (sim>= 0.8) and (cad not in postfix_list):
            postfix_list.append(cad)

match = open("jaro_post.txt", "w")
if match.mode == "w":
    for item in postfix_list:
        match.write("%s\n" % item)
