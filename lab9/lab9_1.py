import time

birth=input('请输入你的出生日期（YYYY-MM-DD）：')
time1=time.strptime(birth,'%Y-%m-%d')
time2=time.localtime()

year=time1.tm_year
month=time1.tm_mon
day=time1.tm_mday
nowyear=time2.tm_year
nowmonth=time2.tm_mon
nowday=time2.tm_mday
age=nowyear-year
if nowmonth>month:
    print('您的周岁为'+str(age))
elif nowmonth==month:
        if day>nowday:
                print('您的周岁为'+str(age-1))
        else :
                print('您的周岁为'+str(age))
else:
    print('您的周岁为'+str(age-1))
