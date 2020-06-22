# coding: utf-8

#交通系ICのみ読み込み可能（？）
#テキストファイルのCardList.txtに書き込まれているIDと一致すると、現在時刻を出力

import nfc
import binascii
import datetime

#*******************************************
def txtFileRead(txt_file_path):
    #ファイルオープン
    f = open(txt_file_path)
    #テキスト読み込み
    strRTN = f.read()
    #ファイルクローズ
    f.close()
    return strRTN

#*******************************************
#*******************************************
#*******************************************
def on_startup(targets):
    #print('on_startup')
    for target in targets:
        # nanaco
        # target.sensf_req = bytearray.fromhex("0004c70000")
        # pasmo
        target.sensf_req = bytearray.fromhex("0000030000")

    return targets


#*******************************************
def on_connect(tag):
    #print('on_connect')
    global strID
    global idm
    
    idm = binascii.hexlify(tag.identifier).upper().decode('utf-8')
    strID = idm
    #strID = idm
    print("readID = " + str(idm))
    return True

#*******************************************
def getTime():
    val = datetime.datetime.now()
    strRTN = str(val.year) + '/' + \
             str(val.month) + '/' + \
             str(val.day) + ' ' + \
             str(val.hour) + ':' + \
             str(val.minute)
    return strRTN

#*************************************************************************************
#*************************************************************************************
#while True:
#print('loop')
with nfc.ContactlessFrontend("usb") as clf:
    #while True:
    rdwr = {
        'targets': ['212F'],
        'on-startup': on_startup,
        'on-connect': on_connect
    }
    clf.connect(rdwr=rdwr)
    
    Card_List = txtFileRead("CardList.txt")
    print("【Card list】")
    print(Card_List)
    
    iHit = Card_List.find(str(strID) + "\n")
    print("Hit = " + str(iHit))
    #print(iHit)
    
    if iHit >= 0:
        #dt_time = datetime.datetime.now()
        T = getTime()
        print(T)
    else:
        print('Error')
    
        #break

