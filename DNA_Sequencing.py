#opens both of the files for reading
sequence = open("suspect1.txt").read()
frag = open("fragment1.txt").read()

#finds the length of the fragment
fragLen = len(frag)

#finds where in the frequence the fragment is first found
fragLoc = sequence.find(frag)

#prints the location of the fragment
print("The fragment is located from position", fragLoc, "to position", fragLen+fragLoc)

