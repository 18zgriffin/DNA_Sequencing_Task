#what number fragement and sequence we are up to in the loop
fragnumber = 0
sequnumber = 0

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

#creates an array with all the frags in it and an array with all the sequences in it
fragarray = [frag1, frag2, frag3, frag4, frag5, frag6]
sequarray = [sequence1, sequence2, sequence3, sequence4, sequence5]

#creates a loop for every fragment, then inside that loop creates a loop for every sequence, it then searches every sequence for a fragment
#and then prints where in the sequence that fragment is, then it loops back and does that for the next fragment
for frag in fragarray:
    print("Fragment Number", fragnumber)
    fragnumber += 1
    sequnumber = 0
    for sequence in sequarray:
        sequnumber += 1
        if frag in sequence:
            fragLoc = sequence.find(frag)
            fragLen = len(frag)
            print("- Found in sequence", sequnumber, " from", fragLoc-1, "to", fragLen+fragLoc)

#finds where in the frequence the fragment is first found


