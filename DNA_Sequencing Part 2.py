#opens all of the files required for reading
sequence1 = open("suspect1.txt").read()
frag1 = open("fragment1.txt").read()
sequence2 = open("suspect2.txt").read()
frag2 = open("fragment2.txt").read()
sequence3 = open("suspect3.txt").read()
frag3 = open("fragment3.txt").read()
sequence4 = open("suspect4.txt").read()
frag4 = open("fragment4.txt").read()
sequence5 = open("suspect5.txt").read()
frag5 = open("fragment5.txt").read()
frag6 = open("fragment6.txt").read()

#finds the length of each fragment
fragLen1 = len(frag1)
fragLen2 = len(frag2)
fragLen3 = len(frag3)
fragLen4 = len(frag4)
fragLen5 = len(frag5)
fragLen6 = len(frag6)


array = [frag1, frag2, frag3, frag4, frag5, frag6]

for frag in array:
    print(frag)
    fragLoc = sequence1.find(frag1)
    print(fragLoc)
#finds where in the frequence the fragment is first found

#prints the location of the fragment
print("The fragment is located from position", fragLoc, "to position", fragLen+fragLoc)

