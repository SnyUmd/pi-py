#SYSの情報がFFFFとなってしまう　原因不明
#PMMは製造コード

import nfc

def on_startup(targets):
    for target in targets: 
        # nanaco 
        # target.sensf_req = bytearray.fromhex("0004c70000")
        # pasmo 
        target.sensf_req = bytearray.fromhex("0000030000")       
    return targets 
 
def on_connect(tag): 
    print(tag) 
    return True # カードが離れるまでに1回のみ  
 
while True: 
    with nfc.ContactlessFrontend("usb") as clf: 
        rdwr = { 
            'targets': ['212F'], # Type3Tag 
            'on-startup': on_startup, 
            'on-connect': on_connect 
        } 
        clf.connect(rdwr=rdwr)
        