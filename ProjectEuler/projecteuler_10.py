#!/usr/bin/env python
# encoding: utf-8
"""

import sys
import os
from scipy import *
from numpy import *

def main():
	j=1
	i=3
	Prime=[2]
	S=2
	while i<2000000:
		if isprime(i,Prime):
			j=j+1
			Prime.append(i)
			S=S+i
		i=i+2
	print S
	
	
def isprime(num,Prime): 
	count = int(sqrt(num)) 
	i=0
	while count >= Prime[i]:
		if num % Prime[i] == 0: return 0 
		i = i + 1 
	return 1
if __name__ == '__main__':
	main()

