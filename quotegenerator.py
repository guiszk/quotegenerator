import sys
import random
import re

if(len(sys.argv) != 2):
    print(f'{sys.argv[0]} <text file>')
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    lines = list(line for line in (l.strip() for l in f) if line)

l = random.choice(lines).strip()
w = random.choice(l.split())
out = ''
match = w.capitalize()

while True:
    matching = [line for line in lines if ' ' + w + ' ' in line and line.strip() != l]
    if(len(matching) > 1):
        matching = random.choice(matching)
        ind = matching.split().index(w) + 1
        w = matching.split()[ind]
        #print(w)
        #print(matching.split()[ind-2:ind+2])
        match += ' ' + w
        if('.' in w):
            break
    else:
        l = random.choice(lines).strip()
        w = random.choice(l.split())
print(match)
