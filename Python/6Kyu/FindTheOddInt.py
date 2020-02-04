# Given an array, find the integer that appears an odd number of times.
# 
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(len(seq)):
            if ( seq [i] == seq[j] ):
                count += 1
        if(count % 2 != 0):
            return seq[i]
        else:
            count = 0
