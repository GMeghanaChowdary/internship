from collections import Counter
s1='listen'
s2='silent'
if len(s1)!=len(s2):
    print('no')
else:
    if Counter(s1)==Counter(s2):
        print("yes")
    else:
        print("no")
