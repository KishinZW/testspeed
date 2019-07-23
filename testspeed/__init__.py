name = "testspeed"
from time import time
from sys import argv
from os import system
tic = time()
system('python %s' % (argv[1]))
toc = time()
print('used %s seconds' % (toc - tic))
