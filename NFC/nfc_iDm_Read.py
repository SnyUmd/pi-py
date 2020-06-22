# coding: utf-8

import nfc
import binascii
import datetime
import subprocess

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#**************************************************************************************
#**************************************************************************************
def speech_man(strTalk):
    subprocess.run(['bash', '/home/pi/_sh/Speech_synthesis/jtalk.sh', strTalk])

def speech_woman(strTalk):
    subprocess.run(['bash', '/home/pi/_sh/Speech_synthesis/jtalk_may.sh', strTalk])
    
#**************************************************************************************
#**************************************************************************************
#Text Ctrl

#テキストファイルの中身を取得
def txtFileRead(txt_file_path):
    #ファイルオープン
    f = open(txt_file_path)
    #テキスト読み込み
    strRTN = f.read()
    #ファイルクローズ
    f.close()
    return strRTN

#*******************************************
def GetID(str_iDm):
    strRTN = ''
    iP0 = str_iDm.find('ID=')
    
    if iP0 < 0:
        return '-1'
    
    iP0 += 3
    
    #IDが何桁あるかにより読み込み文字数を判定
    #iDmの文字数を取得
    iLen = len(str_iDm)
    if iLen - iP0 <= 16:
        strRTN = str_iDm[iP0:iP0 + iLen - iP0]
    else:
        strRTN = str_iDm[iP0:iP0 + 16]
        
    return strRTN
#**************************************************************************************
#**************************************************************************************
#Time Ctrl

#*******************************************
#現在時刻を取得　YYYY/MM/DD hh:mm
def getTime():
    val = datetime.datetime.now()
    strRTN = str(val.year) + '/' + \
             str(val.month) + '/' + \
             str(val.day) + ' ' + \
             str(val.hour) + ':' + \
             str(val.minute)
             #★★★人桁の数字になると、見た目が悪くなるので０埋め使しよう。
    return strRTN


#**************************************************************************************
#**************************************************************************************
#NFC Ctrl

def on_startup(targets):
    for target in targets:
        # nanaco
        # target.sensf_req = bytearray.fromhex("0004c70000")
        # pasmo
        target.sensf_req = bytearray.fromhex("0000030000")       
    return targets

#*******************************************
def on_connect(tag):
    global str_iDm
    str_iDm = str(tag)
    #print(str_iDm)
    return True # カードが離れるまでに1回のみ 

#**************************************************************************************
#**************************************************************************************


while True:
    with nfc.ContactlessFrontend("usb") as clf:
        #-------------------------------------------------------
        rdwr = {
            'targets': ['212F','106A','106B'],  #212F Type3Tag
                                                #106A Type2Tag,Type4ATag
                                                #106B Type4B
            'on-startup': on_startup,
            'on-connect': on_connect
        }
        clf.connect(rdwr=rdwr)
        #-------------------------------------------------------
        
        iP0 = str_iDm.find('ID=')
        if iP0 >= 0:
            iP0 += 3
        else:
            print('Error')
            speech_man('読み込みに失敗しました。')
            continue
        
        print('iP0 = ' + str(iP0))
        print(str_iDm)
        
        time_val = getTime()
        print('time = ' + time_val)
        print(GetID(str_iDm))
        speech_man('読み込みに成功しました。')
        