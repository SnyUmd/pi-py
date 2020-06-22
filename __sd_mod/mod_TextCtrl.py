
#**************************************************
def mTextSplit_Word(str_text, str_split_word):
	strRtn = str_text.split(str_split_word)
	return strRtn

#**************************************************
def mTextSplit_Line(str_text):
	if str_text.count('\n') <= 0:
		print('err : No line break')
                strRTN = 'err'
	else:
		strRTN = str_text.splitlines()	
	return strRTN

#**************************************************
#def mTextRead():



#**************************************************
def mTextSerch_point(strTarget, strSerchWord, iStartPoint, blRear):
    iRTN = -1
    if blRear:
        iRTN = strTarget.rfind(strSerchWord, iStartPoint)
    else:
        iRTN = strTarget.find(strSerchWord, iStartPoint)
    return iRTN

#**************************************************
