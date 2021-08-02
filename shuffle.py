#!/usr/bin/env python3
import os, sys

if os.path.isfile ("offers_to.txt"):
    print ("File offers_to.txt exists. Remove it if you want to restart.")
    sys.exit(1)

with open("participants.txt", 'r') as f:
    participants = [ p.replace('\n','') for p in f ]

participants = [ p for p in participants if p != '' ]

with open("forbidden_pairings.txt", 'r') as f:
    forbidden_pairings = [ (p.split(';')[0],p.split(';')[1]) for p in f ]
    forbidden_pairings = [ (p[0].replace('\n',''), p[1].replace('\n','')) for p in forbidden_pairings]

# n = participant list
# res = list of people to offer to
# f = pairs of forbidden pairings (reciprocal)
def is_OK (n, res, f):
    for i,j in zip(n,res):
        if i == j: #someone should not offer themselves a gift
            return False
        for k,l in f: #the pair should not be forbidden
            if i == k and j == l:
                return False
            if i == l and j == k:
                return False
    return True

def safe_shuffle (n, f):
    from random import shuffle
    res = n[:]
    ok = False
    while not ok:
        shuffle(res)
        ok = is_OK(n, res, f)
    return res

offers_to = safe_shuffle (participants, forbidden_pairings)
offers_to = [ p + '\n' for p in offers_to ]

with open("offers_to.txt", 'w') as f:
    f.writelines (offers_to)

os.chmod ("offers_to.txt", 0o400)
