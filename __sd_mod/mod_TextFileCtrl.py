import sys

def TextFileRead(str_filename):
	f = open(str_filename, 'r')
	return f.read()

def TextFileWrite(str_filename, strVal):
	f = open(str_filename, 'w')
	f.write(strVal)
	f.close()

def TextFileWrite_AddText(str_filename, strAdd):
	t = TextFileRead(str_filename)
	t += strAdd
	TextFileWrite(str_filename, t)

"""
val = TextFileRead('/home/pi/_sd_data/test.txt')
print(val)
"""
