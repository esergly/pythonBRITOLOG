import datetime

textime = "Tue Oct 13 23:47:01 EEST 2020"
timestart = "20/10/14 23:57"
timestart_corr = datetime.datetime.strptime(timestart, '%y/%m/%d %H:%M') + datetime.timedelta(minutes=15)
timestart = "20/11/15 22:47"
timestop = "19/10/15 22:47"

tdelta = datetime.datetime.strptime(timestop, '%y/%m/%d %H:%M') - datetime.datetime.strptime(timestart, '%y/%m/%d %H:%M')
if str(tdelta)[0] == '-':
    print("fault")
else:
    print(tdelta)
# txt_to_stdate = datetime.datetime.strptime(timestart, '%y/%m/%d %H:%M')
# tdelta = dtstop - dtstart
# print(tdelta)
# strftime - Datetime to String
# strptime - String to Datetime

#        print('Дата:', valid_date.date())
#        print('Время:', valid_date.time())
#        print('Дата и время:', valid_date)

resdt = datetime.datetime.strptime(timestart, '%y/%m/%d %H:%M')
resst = datetime.datetime.strftime(datetime.datetime.strptime(timestart, '%y/%m/%d %H:%M'), '%a %b %d %H:%M:%S EEST %Y')
resst_corr = datetime.datetime.strftime(timestart_corr, '%a %b %d %H:%M:%S EEST %Y')

#print(resst, resst_corr, end="\n")

d1 = datetime.datetime.strptime(timestart, "%y/%m/%d %H:%M")
d2 = datetime.datetime.strptime(timestop, "%y/%m/%d %H:%M")
res = abs((d2 - d1).seconds)

#print(res)