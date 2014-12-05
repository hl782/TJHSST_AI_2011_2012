#!/usr/bin/python
#
# Torbert, 12 August 2011
#
# First week example Python program... miscellaneous
#
# Demo of popular functions (methods) from various modules.
# Use 'chmod 755 file.py' and bang line to make executable.
# Timing can also be done with 'time ./file.py', want real.
#
################################################################################
from random import *
from time   import time
#
a=list('helloworld')
shuffle(a)
print a
#
tic=time()
b=[choice(a) for k in range(randint(10,20))]
toc=time()
print b
#
c=[]
for k in xrange(randint(10,20)): # xrange is faster than range
	c.append(choice(a))
c.pop()
c.pop(0)
print c
#
print random()
#
fout=open('misc.txt','w')
fout.write('Hello world!\n')
fout.close()
#
print toc-tic
#
# Notes
# -----
# Sample output:
#    ['e', 'l', 'r', 'h', 'l', 'o', 'o', 'w', 'l', 'd']
#    ['d', 'l', 'r', 'h', 'e', 'l', 'e', 'r', 'r', 'e', 'l', 'o']
#    ['l', 'd', 'l', 'o', 'l', 'e', 'l', 'l', 'w']
#    0.91391043481
#    2.28881835938e-05
#    
#    real    0m0.012s
#    user    0m0.004s
#    sys     0m0.004s
#
################################################################################
#
# end of file
#
