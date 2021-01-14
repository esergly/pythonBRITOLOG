"""
The module which cut the selected by the input time stamps
data from the whole log file.
"""
import sys


def read_the_interval(interval, hc_file):
    """
    :param interval:
    :param hc_file:
    :return:
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
            return result_file
    except IOError:
        print("The source file can't been reading")
        sys.exit()


if __name__ == '__main__':
    period = ('Thu Dec 31 23:47 EET 2020', 'Fri Jan  1 00:19 EET 2021')
    LOG_FILE_SRC = 'short.log'  # used for tests only.
    print(read_the_interval(period, LOG_FILE_SRC),end='\n')

__version__ = '01.21'
