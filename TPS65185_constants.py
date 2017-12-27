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

class REG:
	TMST_VALUE = 0
	ENABLE = 1
	VADJ = 2
	VCOM = 3
	INT_EN1 = 5
	INT_EN2 = 6
	INT1 = 7
	INT2 = 8
	UPSEQ0 = 9
	UPSEQ1 = 10
	DWNSEQ0 = 11
	DWNSEQ1 = 12
	TMST1 = 13
	TMST2 = 14
	PG = 15
	REVID = 16
