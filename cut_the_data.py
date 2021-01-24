"""
The module which cut the selected by the input time stamps
data from the whole log file.
"""
import sys

import read_alarms
import read_counters
import read_services


def read_the_interval(interval, hc_file):
    """
    This function get the set of dates in the str format (the begin and the end points
    of the sliced data from the whole log file) and the name of the log file.
    Then this data stored in the variable

    :param interval: set('str','str')
    :param hc_file: str
    :return: tuple
    """
    result_file = []
    day_time_start = interval[0][:16]
    day_time_stop = interval[1][:16]
    year_start = interval[0][21:]
    year_stop = interval[1][21:]

    try:
        with open(hc_file, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if all([(day_time_start in line), (year_start in line)]):
                    result_file.append(line)
                else:
                    if all([(day_time_stop not in line), (year_stop not in line)]):
                        result_file.append(line)
                    else:
                        break
            return tuple(result_file)
    except IOError:
        print("The source file can't been reading")
        sys.exit()


def choose_task(time_interval, file):
    """

    :param time_interval:
    :param file:
    :return:
    """
    while True:
        _ = input("Please make you choice: \n"
                  "1 for counters data \n"
                  "2 for alarms data \n"
                  "3 for services data \n"
                  "0 for exit: ")
        if _ == "1":
            read_counters.read_counters(read_the_interval(time_interval, file))
        elif _ == "2":
            read_alarms.read_alarms(read_the_interval(time_interval, file))
        elif _ == "3":
            read_services.read_services(read_the_interval(time_interval, file))
        elif _ == "0":
            sys.exit()
        else:
            print("Your choice isn't correct. Please try again.\U0001F504")


if __name__ == '__main__':
    period = ('Thu Dec 31 23:47 EET 2020', 'Fri Jan  1 00:19 EET 2021')  # used for tests only.
    LOG_FILE_SRC = 'short.log'  # used for tests only.
    choose_task(period, LOG_FILE_SRC)
__version__ = '01.21'
