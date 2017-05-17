#!/usr/bin/env python3
def sort(seq):
    # BEGIN (write your solution here)
    END = len(seq)
    while END > 0:
        for i in range(END-1):
            if seq[i+1] < seq[i]:
                seq[i],seq[i+1] = seq[i+1],seq[i]
        END -= 1
    # END
    return seq

print(sort([2,1]))
