import time

def analytime(time1):
    time1=time.strptime(time1,'%Y-%m-%d')
    year=time1.tm_year
    days=time1.tm_yday
    week=time1.tm_wday
    return year,days,week

def judgeyear(a):
    if a%4==0&a%100!=0:
        return True
    elif a%400==0:
        return True
    else:
        return False

if __name__=='__main__':
    time1=input('请输入你解析的日期（YYYY-MM-DD）：')
    year1=(analytime(time1)[0])
    if judgeyear(year1)=='True':
        print('你输入的日期为闰年')
    else:
        print('你输入的日期为平年')
    print('是今年的第'+str(analytime(time1)[1])+'天''星期'+str(analytime(time1)[2]+1))
    