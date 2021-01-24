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
    result_data = []
    day_time_start = interval[0][:16]
    day_time_stop = interval[1][:16]
    year_start = interval[0][21:]
    year_stop = interval[1][21:]
    record_key = True
    try:
        with open(hc_file, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if all([(day_time_start in line), (year_start in line)]):
                    result_data.append(line)
                    record_key = False
                elif all([(day_time_stop in line), (year_stop in line), record_key == False]):
                    result_data.append(line)
                    break
                elif record_key == False:
                    result_data.append(line)

        with open("result.log", 'w', encoding='utf-8') as file:
            for line in result_data:
                file.write(line)
            return tuple(result_data)
    except IOError:
        print("The source file can't been reading.")
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
                  "0 for exit: \n")
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
    period = ('Thu Dec 31 23:32 EET 2020', 'Fri Jan  1 01:17 EET 2021')  # used for tests only.
    LOG_FILE_SRC = 'stat.log'  # used for tests only.
    choose_task(period, LOG_FILE_SRC)
#   print(read_the_interval(period, LOG_FILE_SRC))
__version__ = '01.21'
