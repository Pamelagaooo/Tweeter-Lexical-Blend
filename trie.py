import pygtrie
import math
import sys

# trie for prefix

dictionary1 = open("dict.txt", "r")
if dictionary1.mode == "r":
    handler_d = dictionary1.readlines()

updated_cad_list = list()
updated_candidates = open("updated_candidates.txt", "r")
if updated_candidates.mode == "r":
    handler_c = updated_candidates.readlines()
    for x in handler_c:
        y = x.split()
        updated_cad_list.append(y[0])

# check possible combination in the dictionary for candidates

#dictionary tries t1 & t2 for prefix and postfix

t1 = pygtrie.CharTrie()
# t2 = pygtrie.CharTrie()


for x in handler_d:
    y = x.split()
    t1[y[0]] = True
    # t2[str((y[0])[::-1])] = True

cad_list = list()
current = 0
for candidate in updated_cad_list:
    current += 1
    sys.stdout.write("\r | complete: {}, total: {}".format(current, len(updated_cad_list)))
    if len(candidate) >= 3:
        total_length = len(candidate)
        length = math.floor(total_length * 0.5)
        pref = candidate[:length]
        if (t1.has_subtrie(pref) is True) and (candidate not in cad_list):
            cad_list.append(candidate)

match = open("trie_pre.txt", "w")
if match.mode == "w":
    for item in cad_list:
        match.write("%s\n" % item)

#trie for suffix

import pygtrie
import math
import sys

true_blend_list = list()
true_blend = open("blends.txt", "r")
if true_blend.mode == "r":
    handler_t = true_blend.readlines()
    for x in handler_t:
        y = x.split()
        true_blend_list.append(y[0])

trie_list = list()
true = open("trie_post.txt", "r")
if true.mode == "r":
    handler_e = true.readlines()
    for x in handler_e:
        y = x.split()
        trie_list.append((y[0])[::-1])

matched_list = list()
for term in trie_list:
    if term in true_blend_list:
        matched_list.append(term)

length2 = len(matched_list)
print(length2)

match = open("match_trie.txt", "w")
if match.mode == "w":
    for item in matched_list:
        match.write("%s\n" % item)


dictionary1 = open("dict.txt", "r")
if dictionary1.mode == "r":
    handler_d = dictionary1.readlines()

trie_pre = list()
pre = open("trie_pre.txt", "r")
if pre.mode == "r":
    handler_c = pre.readlines()
    for x in handler_c:
        y = x.split()
        trie_pre.append((y[0])[::-1])

#check possible combination in the dictionary for candidates

#dictionary tries t1 & t2 for prefix and postfix


t2 = pygtrie.CharTrie()


for x in handler_d:
    y = x.split()
    t2[str((y[0])[::-1])] = True

cad_list = list()
current = 0
for candidate in trie_pre:
    current += 1
    sys.stdout.write("\r | complete: {}, total: {}".format(current, len(trie_pre)))
    if len(candidate) >= 3:
        total_length = len(candidate)
        length = math.floor(total_length * 0.5)
        pref = candidate[:length]
        if (t2.has_subtrie(pref) is True) and (candidate not in cad_list):
            cad_list.append(candidate)

match = open("trie_post.txt", "w")
if match.mode == "w":
    for item in cad_list:
        match.write("%s\n" % item)