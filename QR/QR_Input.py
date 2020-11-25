# coding: utf-8
'''
スクリプトファイルのディレクトリに、QRコードのpngファイルが生成される。
'''

import pyqrcode
import sys

args = sys.argv

str = ['', '', '', '']
print('QRコードにするテキストを入力：')
str[1] = input()
print('QRコードのサイズを入力：')
str[2] = input()
print('作成するpngファイル名を入力(拡張子不要)：')
str[3] = input()

a = pyqrcode.create(content=str[1],error= 'H') 
a.png(file=str[3] + '.png',
      scale=str[2],
      module_color=[0, 0, 0, 0],
      background=[255, 255, 255, 255],
      ) 