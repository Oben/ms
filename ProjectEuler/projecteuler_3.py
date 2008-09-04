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
	N=600851475143
	M=int(sqrt(N))
	i=M
	S=[]
	while i>0:
		if mod(N,i) == 0:
			S.append(i)
		i=i-1 
	print S
	P=1
	p=len(S)-2
	while P<N:
		Prime = arange(S[p]+1)
		j=2
		while len(Prime) > j+1:
			for i in range(j+1,len(Prime)):
				if mod(Prime[i],Prime[j])==0:
					Prime[i]=0
			Prime=dict.fromkeys(Prime).keys()
			j=j+1
		if S[p] in Prime:
				P=P*S[p]
				print S[p]
		p=p-1
	pass


if __name__ == '__main__':
	main()

