#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Ben BarOr on 2008-08-23.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from scipy import *
from numpy import *

def main():
	j=1
	i=3
	Prime=[2]
	while j<10001:
		if isprime(i,Prime):
			j=j+1
			Prime.append(i)
		i=i+2
	print Prime[10001-1]
	
def isprime(num,Prime): 
	count = int(sqrt(num)) 
	i=0
	while count >= Prime[i]:
		if num % Prime[i] == 0: return 0 
		i = i + 1 
	return 1
if __name__ == '__main__':
	main()

