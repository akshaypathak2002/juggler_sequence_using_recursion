# To find juggler sequence of number
''' A juggler sequence is that in which we start with a term 3 then if it is evne then it power is 1/2 and if odd then it power is 3/2 and 

in recurssion we known that what we can do it if 1 then return 0 
'''
import math


def jum_sequence(N):
    print(N)
    if (N == 1):
        return
    elif N & 1 == 0:
        N = int(pow(N, 0.5))
        jum_sequence(N)
    else:
        N = int(pow(N, 1.5))
        jum_sequence(N)


jum_sequence(10)
