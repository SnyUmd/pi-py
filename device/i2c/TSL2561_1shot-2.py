# -*- coding: utf-8 -*-
import smbus
import time

class clsI2C:
    def setI2C(self, DeviceAddress):
        self.bus = smbus.SMBus(1)
        self.address = DeviceAddress
        self.write8(0x80, 0x03)# 0x03=PowerON 0x00=PowerOFF

    def write8(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except IOError, err:
            print "IO Error"

    def readU16(self, reg):
        try:
            result = self.bus.read_word_data(self.address,reg)
            return result
        except IOError, err:
            print "IO Error"
            return 0

    def setParam(self, RegisterAddress, Parameters):
        self.write8(RegisterAddress, Parameters)

    def readData(self,ReadAddress):
        #return self.readU16(0xAC)
        return self.readU16(ReadAddress)

#**************************************************************************
if __name__ == "__main__":
    prmINT = 2      #integate time
                    #0:13.7ms(scale 0.034)
                    #1:101ms(scale 0.252)
                    #2:402ms(scale 1)
                    #3:N/A
                
    prmManual = 0   #Manual timing control
                    #0:stops integration cycle
                    #1:begins an integration cycle
                    
    prmGain = 0     #Gain control
                    #0:x1
                    #1:x16
                    
    prmSet = prmINT + (prmManual << 3) + (prmGain << 4)#Integrate and gain parameter set
    
    tsl = clsI2C()
    tsl.setI2C(0x39)#device address set
    tsl.write8(0x80, 0x03)#Power on:0x03 off:0x00
    #time.sleep(1)#Power on wait 
    tsl.write8(0x81, prmSet)#Integrate and gain set
    print tsl.readData(0xAC)

#******************************************************************
