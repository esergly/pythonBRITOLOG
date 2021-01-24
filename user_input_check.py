"""
This module is for checking of the input data.

Used to get the answer either an user has input all necessary data in the correct
form (data, path to the log file) or not.

As example:
- input date by user is:
20/11/13 11:22 or 20/12/01 10:50

- output date on user's screen is:
Fri Nov 13 11:22:00 EET 2020 or Tue Dec 01 10:50:00 EET 2020

- corrected output date used in log file is:
Fri Nov 13 11:32:00 EET 2020 or Tue Dec  1 11:02:00 EET 2020
!!! Shifted time and changed day number format !!!
"""

import sys
from datetime import datetime, timedelta


def date_check(period):
    """
    The function is for check the input date.

    We get the input date and check it correction of:
    - are the all parameters have been entered and it have done in the correct form
    (the length must be == 14)?;
    - want user to stop (word "exit" used as input data)?
    - if input date is in correct form it will changed to the nearest date which is
    present in the log file;

    :param period: str
    :return: datetime
    """
    if period == "exit":
        sys.exit()
    elif len(period) == 14:
        try:
            valid_date = datetime.strptime(period, '%y/%m/%d %H:%M')
        except ValueError:
            print("Input date isn't correct. Please try again. \U0001F504")
            return -1
        # In the log file we have values for each 15 min beginning from the second min of each hour.
        # The idea is to find the nearest biggest time value and use it in the parsing.
        # For example, the data for 10:15 will collect at 10:17, but for 10:18 will collect at 10:32
        minute = datetime.strftime(valid_date, '%M')

        if 2 <= int(minute) <= 16:
            correction = 17 - int(minute)
        elif 17 <= int(minute) <= 31:
            correction = 32 - int(minute)
        elif 32 <= int(minute) <= 46:
            correction = 47 - int(minute)
        elif 47 <= int(minute) <= 59:
            correction = 62 - int(minute)
        else:
            correction = 2 - int(minute)
        _ = datetime.strptime(period, '%y/%m/%d %H:%M')
        period_correction = _ + timedelta(minutes=correction)
        # return corrected input by user date which can be use for the file log parsing.
        return period_correction
    else:
        print("Entered date isn't correct format. Would you please input it once again? \U0001F504")
        return -1


def log_file_check(input_date, file_sr):
    """
    This function uses to check the wanted dates in log file.
    In case of this log file is present in the working folder.

    After getting the input date correction we use it for the log file checking:
    - check that the log file is present in the working folder;
    - check if the input date is present in the log file;
    :param input_date: datetime
    :param file_sr: str
    :return: str
    """
    day = datetime.strftime(input_date, '%b %d')
    year = datetime.strftime(input_date, '%Y')

    # The date of days collected in the log files have format 1, 2, 3... 11, 12 e.t.c.
    # We need to covert standard datetime format to the format presents in the log file.
    if day[4] == '0':
        day = day[0:4] + ' ' + day[5]
    try:
        with open(file_sr, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if all([(day in line), (year in line)]):
                    result = datetime.strftime(input_date, '%a %b %d %H:%M EET %Y')
                    return result
            print("This date isn't present in the log file.\U0001F504")
            return -1
    except FileNotFoundError:
        print("The source file wasn't found in the working folder.")
        sys.exit()


def set_of_intervals(log_file_sr):
    """
    The function is for set dates interval.

    This function asks user to input START and STOP dates (one by one) and times
    which will use to create time's interval to get collected data.

    :param log_file_sr: str
    :return: str
    """
    while True:
        start = input("Please set START date YY/MM/DD HH:MM ('exit' to stop): ")
        if date_check(start) != -1 and log_file_check(date_check(start), log_file_sr) != -1:
            # Is everything ok? Prepare separated outputs of the input START date:
            # for user and for us.
            period_start_log = log_file_check(date_check(start), log_file_sr)
            _ = datetime.strptime(start, '%y/%m/%d %H:%M')
            instart = datetime.strftime(_, '%a %b %d %H:%M EET %Y')
            break
    while True:
        stop = input("Please set END date YY/MM/DD HH:MM ('exit' to stop): ")
        if date_check(stop) != -1:
            # We check here can we collect data between input dates:
            # is STOP date is elder than START date?
            date_stop = datetime.strptime(stop, '%y/%m/%d %H:%M')
            date_start = datetime.strptime(start, '%y/%m/%d %H:%M')
            period_delta = date_stop - date_start
            if str(period_delta)[0] == '-':
                print("The END date is less then START date. Please try again. \U0001F504")
            else:
                if (date_check(stop)) != -1 and log_file_check(date_check(stop), log_file_sr) != -1:
                    # Is everything ok? Prepare separated outputs of the input START date:
                    # for user and for us.
                    period_stop_log = log_file_check(date_check(stop), log_file_sr)
                    _ = datetime.strptime(stop, '%y/%m/%d %H:%M')
                    instop = datetime.strftime(_, '%a %b %d %H:%M EET %Y')
                    break
    # The dates collected in the log files have format 1, 2, 3... 11, 12 e.t.c.
    # We need to covert standard datetime format to the format presents in the log file.
    # The same story but now for the final output result.
    if period_start_log[8] == "0":
        period_start_log = period_start_log[:8] + ' ' + period_start_log[9:]

    if period_stop_log[8] == "0":
        period_stop_log = period_stop_log[:8] + ' ' + period_stop_log[9:]

    print("\n*******************************************")
    print(f'        The period has been chosen!         \n- From -> {instart} \n- To  ->  {instop}')
    print("*******************************************\n")
    return period_start_log, period_stop_log


if __name__ == '__main__':
    LOG_FILE_SRC = 'stat.log'  # used for tests only.
    set_of_intervals(LOG_FILE_SRC)

__version__ = '01.21'
