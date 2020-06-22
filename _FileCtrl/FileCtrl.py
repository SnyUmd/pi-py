# coding: utf-8

def txtFileRead(txt_file_path):
    #ファイルオープン
    f = open(txt_file_path)
    #テキスト読み込み
    strRTN = f.read()
    #ファイルクローズ
    f.close()
    return strRTN