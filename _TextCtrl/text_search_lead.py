# coding: utf-8

import sys

args = sys.argv
strBase = args[1]
strTarget = args[2]

iLen = len(strTarget)
iPoint = strBase.find(strTarget)

if iPoint < 0:
	print(iPoint)
else:
	print(iPoint + iLen)

