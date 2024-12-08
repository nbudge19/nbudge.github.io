import datetime

def day(time1,time2):
    list1=time1.split('-')
    list2=time2.split('-')
    t1=datetime.date(int(list1[0]),int(list1[1]),int(list1[2]))
    t2=datetime.date(int(list2[0]),int(list2[1]),int(list2[2]))
    numday=t2-t1
    return numday.days

if __name__=='__main__':
    date1=input('请输入起始日期（如：2020-01-01）：')
    date2=input('请输入终止日期（如：2020-12-31）：')
    numday=day(date1,date2)
    print(numday)

    benjin=int(input('请输入本金：'))
    rate=2.75
    interest=benjin*rate/100*numday/365

    print('利息为：%d' %interest)