import sys

sys.path.append("/home/pi/_py/__sd_mod")
import modTextFileCtrl as tc

a = sys.argv

if len(a) <= 1:
	print('none')
else:
	print(a[1])
"""
tc.TextFileWrite_AddText('/home/pi/_sd_data/test.txt', 'Add2')
val = tc.TextFileRead('/home/pi/_sd_data/test.txt')
print(val)
"""

"""
test
"""
