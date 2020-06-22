# -*- coding: utf-8 -*-
import smbus
import time

adr = 0x40
flg_loop = True
cnt = 0

prmOPT_Reload = 1 << 1          #有効にしない。リロードするときはソフトリセットを行うこと
prmOnChipHeater = 0 << 2        #機能診断をする際に使用する。
                                #ヒーターで0.5~1.5度上昇指させた時に湿度が低下すれば正常
                                
prmEndOfBattery = 1 << 6        #0:VDD > 2.25V
                                #1:VDD < 2.25V
                    
prmResolution0 = 0 << 0         #bit7,0
prmResolution7 = 0 << 7         #00:RH-12bit T-14bit
                                #01:RH-8bit  T-12bit
                                #10:RH-10bit T-13bit
                                #11:RH-11bit T-11bit
    
prmSet = prmOPT_Reload + prmOnChipHeater + prmEndOfBattery + prmResolution7 + prmResolution0 #Integrate and gain parameter set

i2c = smbus.SMBus(1)
time.sleep(0.1)
i2c.write_byte_data(adr, 0xE6, prmSet)
time.sleep(0.1)

#-----------------------------------------------
while flg_loop:
        try:
                val_data = i2c.read_i2c_block_data(adr,0xF3,3)
                #print(hex(val_data[0]))
                print(hex(val_data[1]))
                print(hex(val_data[2]))
                print("cnt = " + str(cnt))
                cnt = 0
                flg_loop = False
        except:
                cnt = cnt + 1
                if cnt > 200:
                        flg_loop = False
                        print("time out err")
                else:
                        time.sleep(1)
                        pass
