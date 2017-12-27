#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""TPS65185: Single chip PMIC for E Ink (R) Vizplex (TM) Enabled Electronic Paper Display"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Texas Instruments"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from TPS65185_constants import *

# name:        TPS65185
# description: Single chip PMIC for E Ink (R) Vizplex (TM) Enabled Electronic Paper Display
# manuf:       Texas Instruments
# version:     0.1
# url:         http://www.ti.com/lit/ds/symlink/tps65185.pdf
# date:        2016-08-01


# Derive from this class and implement read and write
class TPS65185_Base:
	"""Single chip PMIC for E Ink (R) Vizplex (TM) Enabled Electronic Paper Display"""
	# Register TMST_VALUE
	# Thermistor value read by ADC signed int, in ˚C
	#       1111 0110 – < -10°C
	#       1111 0110 – -10°C
	#       1111 0111 – -9°C
	#       ...
	#       1111 1110 – -2°C
	#       1111 1111 – -1°C
	#       0000 0000 – 0°C
	#       0000 0001 – 1°C
	#       0000 0010 – 2°C
	#       ...
	#       0001 1001 – 25°C
	#       ...
	#       0101 0101 – 85°C 
	#       0101 0101 – > 85°C 
	
	
	def setTMST_VALUE(self, val):
		"""Set register TMST_VALUE"""
		self.write(REG.TMST_VALUE, val, 8)
	
	def getTMST_VALUE(self):
		"""Get register TMST_VALUE"""
		return self.read(REG.TMST_VALUE, 8)
	
	# Bits TEMP
	# Register ENABLE
	# Enable/disable bits for regulators 
	
	def setENABLE(self, val):
		"""Set register ENABLE"""
		self.write(REG.ENABLE, val, 8)
	
	def getENABLE(self):
		"""Get register ENABLE"""
		return self.read(REG.ENABLE, 8)
	
	# Bits ACTIVE
	# 1 = Transition from STANDBY to ACTIVE mode. Rails power up as defined by UPSEQx
	#           registers.
	#           0 = No effect.
	#           NOTE: After transition bit is cleared automatically 
	
	# Bits STANDBY
	# Transition from STANDBY to ACTIVE mode. Rails power up as defined by DWNSEQx
	#           registers.
	#           NOTE: After transition bit is cleared automatically.
	#           STANDBY bit has priority over AVTIVE. 
	
	# Bits V3P3_EN
	# VIN3P3 to V3P3 switch enable (1=ON) 
	# Bits VCOM_EN
	# VCOM buffer enable (1 = enabled) 
	# Bits VDDH_EN
	# VDDH charge pump enable (1 = enabled) 
	# Bits VPOS_EN
	# VPOS LDO regulator enable. (1 = enabled)
	#           NOTE: VPOS cannot be enabled before VNEG is enabled. 
	
	# Bits VEE_EN
	# VEE charge pump enable (1 = enabled) 
	# Bits VNEG_EN
	# VNEG LDO regulator enable. (1 = enabled)
	#           NOTE: When VNEG is disabled VPOS will also be disabled. 
	
	# Register VADJ
	# VPOS/VNEG voltage adjustment 
	
	def setVADJ(self, val):
		"""Set register VADJ"""
		self.write(REG.VADJ, val, 8)
	
	def getVADJ(self):
		"""Get register VADJ"""
		return self.read(REG.VADJ, 8)
	
	# Bits unused_0
	# Bits VSET
	# VPOS and VNEG voltage setting 
	# Register VCOM
	# VCOM voltage setting, byteorder little 
	
	def setVCOM(self, val):
		"""Set register VCOM"""
		self.write(REG.VCOM, val, 16)
	
	def getVCOM(self):
		"""Get register VCOM"""
		return self.read(REG.VCOM, 16)
	
	# Bits ACQ
	# Kick-back voltage acquisition bit.
	#           1 - starts kick-back voltage measurement routine.
	#           NOTE: After measurement is complete bit is cleared automatically and measurement
	#           result is reflected in VCOM[8:0] bits. 
	
	# Bits PROG
	# VCOM programming bit.
	#           1 - VCOM[8:0] value is committed to nonvolatile memory and becomes new power-up
	#               default.
	#           NOTE: After programming bit is cleared automatically and TPS65185 will enter
	#           STANDBY mode. 
	
	# Bits HiZ
	# VCOM HiZ bit.
	#           1 - VCOM pin is placed into hi-impedance state to allow VCOM measurement
	#           0 - VCOM amplifier is connected to VCOM pin 
	
	# Bits AVG
	# Number of acquisitions that is averaged to a single kick-back voltage measurement
	#           NOTE: When the ACQ bit is set, the state machine repeat the A/D conversion of the
	#           kick-back voltage AVD[1:0] times and returns a single, averaged, value to VCOM[8:0] 
	
	# Bits unused_0
	# Bits VCOM
	# VCOM voltage adjustment
	#           VCOM = -10 mV * VCOM[8:0] in the range from 0 mV to -5.110 V
	#           0x000h – 0 0000 0000 – –0 mV
	#           0x001h – 0 0000 0001 – –10 mV
	#           0x002h – 0 0000 0010 – –20 mV
	#           ...
	#           0x07Dh - 0 0111 1101 – –1250 mV
	#           ...
	#           0x1FEh – 1 1111 1110 – –5100 mV
	#           0x1FFh – 1 1111 1111 – –5110 mV
	#         
	
	# Register INT_EN1
	# Interrupt enable group1 
	# 1 = enabled, 0 = disabled 
	
	
	def setINT_EN1(self, val):
		"""Set register INT_EN1"""
		self.write(REG.INT_EN1, val, 8)
	
	def getINT_EN1(self):
		"""Get register INT_EN1"""
		return self.read(REG.INT_EN1, 8)
	
	# Bits DTX_EN
	# Panel temperature-change interrupt enable
	# Bits TSD_EN
	# Thermal shutdown interrupt enable
	# Bits HOT_EN
	# Thermal shutdown early warning enable
	# Bits TMST_HOT_EN
	# Thermistor hot interrupt enable
	# Bits TMST_COLD_EN
	# Thermistor cold interrupt enable
	# Bits UVLO_EN
	# VIN under voltage detect interrupt enable
	# Bits ACQC_EN
	# VCOM acquisition complete interrupt enable
	# Bits PRGC_EN
	# VCOM programming complete interrupt enable
	# Register INT_EN2
	# Interrupt enable group2 
	# 1 = enabled, 0 = disabled 
	
	
	def setINT_EN2(self, val):
		"""Set register INT_EN2"""
		self.write(REG.INT_EN2, val, 8)
	
	def getINT_EN2(self):
		"""Get register INT_EN2"""
		return self.read(REG.INT_EN2, 8)
	
	# Bits VBUVEN
	# Positive boost converter under voltage detect interrupt enable
	# Bits VDDHUVEN
	# VDDH under voltage detect interrupt enable
	# Bits VNUV_EN
	# Inverting buck-boost converter under voltage detect interrupt enable
	# Bits VPOSUVEN
	# VPOS under voltage detect interrupt enable
	# Bits VEEUVEN
	# VEE under Voltage detect interrupt enable
	# Bits VCOMFEN
	# VCOM FAULT interrupt enable
	# Bits VNEGUVEN
	# VNEG under Voltage detect interrupt enable
	# Bits EOCEN
	# Temperature ADC end of conversion interrupt enable
	# Register INT1
	# Interrupt group1 DEFAULT '0xxxxx00 
	
	def setINT1(self, val):
		"""Set register INT1"""
		self.write(REG.INT1, val, 8)
	
	def getINT1(self):
		"""Get register INT1"""
		return self.read(REG.INT1, 8)
	
	# Bits DTX
	# Panel temperature-change interrupt, 1 - temperature has changed by 3 deg or more
	#           over previous reading 
	
	# Bits TSD
	# Thermal shutdown interrupt
	# Bits HOT
	# Thermal shutdown early warning
	# Bits TMST_HOT
	# Thermistor hot interrupt. 1 - thermistor temperature is equal or greater than
	#           TMST_HOT threshold 
	
	# Bits TMST_COLD
	# Thermistor cold interrupt. 1 - thermistor temperature is equal or less than
	#           TMST_COLD threshold 
	
	# Bits UVLO
	# VIN under voltage detect interrupt. 1 - input voltage is below UVLO threshold 
	# Bits ACQC
	# VCOM acquisition complete
	# Bits PRGC
	# VCOM programming complete
	# Register INT2
	# Interrupt group2 
	
	def setINT2(self, val):
		"""Set register INT2"""
		self.write(REG.INT2, val, 8)
	
	def getINT2(self):
		"""Get register INT2"""
		return self.read(REG.INT2, 8)
	
	# Bits VB_UV
	# Positive boost converter undervoltage detect interrupt 1 - under-voltage on
	#          DCDC1 detected 
	
	# Bits VDDH_UV
	# VDDH under voltage detect interrupt on VDDH charge pump 
	# Bits VN_UV
	# Inverting buck-boost converter under voltage detect interrupt 1 -
	#           undervoltage on DCDC2 detected 
	
	# Bits VPOS_UV
	# VPOS undervoltage detect interrupt 1 - undervoltage on LDO1(VPOS) detected 
	# Bits VEE_UV
	# VEE undervoltage detect interrupt 1 - undervoltage on VEE charge pump detected 
	# Bits VCOMF
	# VCOM fault detection 1 - fault on VCOM detected
	#           (VCOM is outside normal operating range) 
	
	# Bits VNEG_UV
	# VNEG undervoltage detect interrupt  1 - undervoltage on LDO2(VNEG) detected 
	# Bits EOC
	# ADC end of conversion interrupt 1 - ADC conversion is complete
	#           (temperature acquisition is complete) 
	
	# Register UPSEQ0
	# Power-up strobe assignment 
	
	def setUPSEQ0(self, val):
		"""Set register UPSEQ0"""
		self.write(REG.UPSEQ0, val, 8)
	
	def getUPSEQ0(self):
		"""Get register UPSEQ0"""
		return self.read(REG.UPSEQ0, 8)
	
	# Bits VDDH_UP
	# VDDH power-up order 
	# Bits VPOS_UP
	# VPOS power-up order 
	# Bits VEE_UP
	# VEE power-up order 
	# Bits VNEG_UP
	# VNEG power-up order 
	# Register UPSEQ1
	# Power-up sequence delay times 
	
	def setUPSEQ1(self, val):
		"""Set register UPSEQ1"""
		self.write(REG.UPSEQ1, val, 8)
	
	def getUPSEQ1(self):
		"""Get register UPSEQ1"""
		return self.read(REG.UPSEQ1, 8)
	
	# Bits UDLY4
	# DLY4 delay time set; defines the delay time from STROBE3 to STROBE4 
	# Bits UDLY3
	# DLY3 delay time set; defines the delay time from STROBE2 to STROBE3 
	# Bits UDLY2
	# DLY2 delay time set; defines the delay time from STROBE1 to STROBE2  
	# Bits UDLY
	# DLY1 delay time set; defines the delay time from VN_PG high to STROBE1 
	# Register DWNSEQ0
	# Power-down strobe assignment 
	
	def setDWNSEQ0(self, val):
		"""Set register DWNSEQ0"""
		self.write(REG.DWNSEQ0, val, 8)
	
	def getDWNSEQ0(self):
		"""Get register DWNSEQ0"""
		return self.read(REG.DWNSEQ0, 8)
	
	# Bits VDDH_DWN
	# VDDH power-down order 
	# Bits VPOS_DWN
	# VPOS power-down order 
	# Bits VEE_DWN
	# VEE power-down order 
	# Bits VNEG_DWN
	# VNEG power-down order 
	# Register DWNSEQ1
	# Power-down sequence delay times 
	
	def setDWNSEQ1(self, val):
		"""Set register DWNSEQ1"""
		self.write(REG.DWNSEQ1, val, 8)
	
	def getDWNSEQ1(self):
		"""Get register DWNSEQ1"""
		return self.read(REG.DWNSEQ1, 8)
	
	# Bits DDLY4
	# DLY4 delay time set; defines the delay time from STROBE3 to STROBE4 
	# Bits DDLY3
	# DLY3 delay time set; defines the delay time from STROBE2 to STROBE3 
	# Bits DDLY2
	# DLY2 delay time set; defines the delay time from STROBE1 to STROBE2 
	# Bits DDLY1
	# DLY2 delay time set; defines the delay time from WAKEUP low to STROBE1 
	# Bits DFCTR
	# At power-down delay time DLY2[1:0], DLY3[1:0], DLY4[1:0] are multiplied with DFCTR[1:0] 
	# Register TMST1
	# Thermistor configuration 
	
	def setTMST1(self, val):
		"""Set register TMST1"""
		self.write(REG.TMST1, val, 8)
	
	def getTMST1(self):
		"""Get register TMST1"""
		return self.read(REG.TMST1, 8)
	
	# Bits READ_THERM
	# Read thermistor value. 1 - initiates temperature acquisition
	#           NOTE: Bit is self-cleared after acquisition is completed 
	
	# Bits unused_0
	# Bits CONV_END
	# ADC conversion done flag
	# Bits unused_1
	# Bits unused_2
	# Bits unused_3
	# Bits DT
	# Panel temperature-change interrupt threshold DTX interrupt is issued when
	#           difference between most recent temperature reading and baseline temperature
	#           is equal to or greater than threshold value. See Hot, Cold, and
	#           Temperature-Change Interrupts for details. 
	
	# Register TMST2
	# Thermistor register 2: hot/cold temperature setting,
	#       default cold=0C, hot=50C 
	
	
	def setTMST2(self, val):
		"""Set register TMST2"""
		self.write(REG.TMST2, val, 8)
	
	def getTMST2(self):
		"""Get register TMST2"""
		return self.read(REG.TMST2, 8)
	
	# Bits TMST_COLD
	# Thermistor COLD threshold
	#           NOTE: An interrupt is issued when thermistor temperature is equal or less
	#           than COLD threshold
	#           temp = -7C + TMST_COLD 
	
	# Bits TMST_HOT
	# Thermistor HOT threshold
	#           NOTE: An interrupt is issued when thermistor temperature is equal or greater
	#           than HOT threshold
	#           temp = 42C + TMST_HOT 
	
	# Register PG
	# Power good status each rails 
	
	def setPG(self, val):
		"""Set register PG"""
		self.write(REG.PG, val, 8)
	
	def getPG(self):
		"""Get register PG"""
		return self.read(REG.PG, 8)
	
	# Bits VB_PG
	# Positive boost converter power good. 1 - DCDC1 is in regulation
	# Bits VDDH_PG
	# VDDH power good. 1 - VDDH charge pump is in regulation
	# Bits VN_PG
	# Inverting buck-boost power good. 1 - DCDC2 is in regulation
	# Bits VPOS_PG
	# VPOS power good. 1 - LDO1(VPOS) is in regulation
	# Bits VEE_PG
	# VEE power good. 1 - VEE charge pump is in regulation
	# Bits unused_0
	# Bits VNEG_PG
	# VNEG power good. 1 - LDO2(VNEG) is in regulation
	# Bits unused_1
	# Register REVID
	# Device revision ID information 
	
	def setREVID(self, val):
		"""Set register REVID"""
		self.write(REG.REVID, val, 8)
	
	def getREVID(self):
		"""Get register REVID"""
		return self.read(REG.REVID, 8)
	
	# Bits MJREV
	# Bits MNREV
	# Bits VERSION
