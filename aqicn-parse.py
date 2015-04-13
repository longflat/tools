#!/usr/bin/env python
import sys, re

while True:
	a = sys.stdin.readline()
	if a == '': break
	m = re.search(">(\d{2,3})<", a)
	if m: print m.group(1)
