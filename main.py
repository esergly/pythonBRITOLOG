##!/usr/bin/env python3 - убрать #, если установлю Python 3.9 на ноде!
"""
The tool for parsing Health check Bridging It file.
"""
import datetime
import sys


def date_check(period):
    """
    добавить описание
    """
    if period == "exit":
        sys.exit()
    elif len(period) == 14:
        try:
            valid_date = datetime.datetime.strptime(period, '%y/%m/%d %H:%M')
        except ValueError:
            print("Input date isn't correct. Please try again. \U0001F504")
            return -1

        minute = datetime.datetime.strftime(valid_date, '%M')
        day = datetime.datetime.strftime(valid_date, '%b %d')
        year = datetime.datetime.strftime(valid_date, '%Y')

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
        period_correction = datetime.datetime.strptime(period, '%y/%m/%d %H:%M') + datetime.timedelta(
            minutes=correction)
        hcfile = 'stat.log'
        try:
            with open(hcfile, 'r', encoding='utf-8') as log_file:
                for line in log_file:
                    if all([(day in line), (year in line)]):
                        return datetime.datetime.strftime(period_correction, '%a %b %d %H:%M:%S EEST %Y')
                else:
                    print("This date isn't present in the log file. Would you please input it once again?")
                    return -1
        except FileNotFoundError:
            print("The source file isn't found in your working folder.")
    else:
        print("Entered date isn't correct format. Would you please input it once again? ")
        return -1


def set_of_intervals():
    """
    The function of set dates interval.

    This function asks to input start and finish dates which will use to create time's
    interval to get collected data.
    """
    while True:
        period_start = input("Please set start date in format like 'YY/MM/DD HH:MM' or enter 'exit' to stop: ")
        if date_check(period_start) != -1:
            period_start_log = date_check(period_start)
            break
    while True:
        period_end = input("Please set end date in format like 'YY/MM/DD HH:MM' or enter 'exit' to stop: ")
        if date_check(period_end) != -1:
            period_delta = datetime.datetime.strptime(period_end, '%y/%m/%d %H:%M') - datetime.datetime.strptime(period_start,
                                                                                                           '%y/%m/%d %H:%M')
            if str(period_delta)[0] == '-':
                print("The End date is less then Start date. Please try again. \U0001F504")
            else:
                period_end_log = date_check(period_end)
                break

    psdt = datetime.datetime.strftime(datetime.datetime.strptime(period_start, '%y/%m/%d %H:%M'),
                                      '%a  %b %d %H:%M:%S EEST %Y')
    pedt = datetime.datetime.strftime(datetime.datetime.strptime(period_end, '%y/%m/%d %H:%M'),
                                      '%a %b %d %H:%M:%S EEST %Y')
    print(period_start_log)
    print(period_end_log)
    print("*************************************************")
    print(f'We will start \nfrom {psdt} \nto   {pedt}')


if __name__ == '__main__':
    set_of_intervals()

#    print(set_of_intervals.__doc__)
# period_end_log = datetime.datetime.strftime(datetime.datetime.strptime(period_start, '%y/%m/%d %H:%M') + datetime.timedelta(minutes=30), '%a %b %d %H:%M:%S EEST %Y')
# Tue Oct 13 23:32:02 EEST 2020
