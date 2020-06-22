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
        return self.readU16(ReadAddress)
