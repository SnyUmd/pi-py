# -*- coding: utf-8 -*-
import smbus
import time

class clsI2C:
    def setI2C(self, DeviceAddress):
        self.bus = smbus.SMBus(1)
        self.address = DeviceAddress

    def write8(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except IOError, err:
            print "err"

    def readU16(self, reg, read_len):
        try:
            self.bus.read_i2c_block_data(reg)
            return result
        except IOError, err:
            print "err"
            return 0

    def setParam(self, RegisterAddress, Parameters):
        self.write8(RegisterAddress, Parameters)

    def readData16(self,ReadAddress):
        return self.readU16(ReadAddress)
        
    def i2cRead(self, reg, read_len):
        try:
            return self.bus.read_i2c_block_data(self.address, reg, read_len)
        except:
            return "err"
        
#**************************************************************************
if __name__ == "__main__":
    prmOPT_Reload = 1 << 1          #有効にしない。リロードするときはソフトリセットを行うこと
    
    prmOnChipHeater = 0 << 2    #機能診断をする際に使用する。
                                #ヒーターで0.5~1.5度上昇指させた時に湿度が低下すれば正常
    
    prmEndOfBattery = 1 << 6    #0:VDD > 2.25V
                                #1:VDD < 2.25V
                    
    prmResolution0 = 1 << 0      #bit7,0
    prmResolution7 = 1 << 7      #00:RH-12bit T-14bit
                                #01:RH-8bit  T-12bit
                                #10:RH-10bit T-13bit
                                #11:RH-11bit T-11bit
                                
    t_res = 16
    rh_res = 16
    
    prmSet = prmOPT_Reload + prmOnChipHeater + prmEndOfBattery + prmResolution7 + prmResolution0 #Integrate and gain parameter set
    
    tsl = clsI2C()
    tsl.setI2C(0x40)#device address set
    time.sleep(1)
    tsl.write8(0xE6, prmSet)#Integrate and gain set
    
    while True:
        val_t = tsl.i2cRead(0xE3, 3)
        val_rh = tsl.i2cRead(0xE5, 3)
    
        val = (val_t[1] << 8) + val_t[2]
        Temper = -46.85 + (175.72 * val / (2**t_res))
        val = (val_rh[1] << 8) + val_rh[2]
        Humidity = -6 + (125 * val / (2**rh_res))

        #print("T = " + str(hex(val_t[1])) + " " + str(hex(val_t[2])))
        print("T = " + str(Temper))
        #print("RH = " + str(hex(val_rh[1])) + " " + str(hex(val_rh[2])))
        print("RH = " + str(Humidity))
        
        time.sleep(1)
#******************************************************************
