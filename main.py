##!/usr/bin/env python3 - убрать #, если установлю Python 3.9 на ноде!
"""
The tool for parsing Health check Bridging It file.
"""

import cut_the_data
import user_input_check

if __name__ == '__main__':
    HEALTH_CHECK_LOG = 'stat.log'
    c = user_input_check.set_of_intervals(HEALTH_CHECK_LOG)
# приходит после проверки даты ('Thu Dec 31 23:47 EET 2020', 'Fri Jan  1 00:17 EET 2021')
    cut_the_data.choose_task(c, HEALTH_CHECK_LOG)
__version__ = '01.21'
