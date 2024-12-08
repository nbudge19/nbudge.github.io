import time
    
def judgeyear(a):
    if a%4==0&a%100!=0:
        return True
    elif a%400==0:
        return True
    else:
        return False

if __name__=='__main__':
    time1=time.localtime()
    year=time1.tm_year
    days=time1.tm_yday
    week=time1.tm_wday
    hour=time1.tm_hour
    min=time1.tm_min
    sec=time1.tm_sec
    if judgeyear(year)=='True':
        print('当前日期为闰年')
    else:
        print('当前日期为平年')
    print('是今年的第'+str(days)+'天''星期'+str(week+1))
    print('现在是'+str(hour)+':'+str(min)+':'+str(sec))
    