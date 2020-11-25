# coding: utf-8
'''
スクリプトファイルのディレクトリに、QRコードのpngファイルが生成される。
コマンド引数　QRコード化するテキスト サイズ ファイル名(拡張子不要)
'''

import pyqrcode
import sys

args = sys.argv

a = pyqrcode.create(content=args[1],error= 'H') 
a.png(file=args[3] + '.png',
      scale=args[2],
      module_color=[0, 0, 0, 0],
      background=[255, 255, 255, 255],
      ) 