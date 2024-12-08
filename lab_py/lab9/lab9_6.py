import threading,time
result=''
def inputa():
    global result
    while 1:
        result=input('请输入内容（输入‘end’结束）：')
        if result=='end':
           break

def writefile(interval):
    global result
    while 1:
        time.sleep(interval)
        f=open('jilu.txt','a')
        str1=result+'\n'
        f.write(str1)
        f.close()

def test():
    t1=threading.Thread(target=inputa,args=())
    t2=threading.Thread(target=writefile,args=(5,))
    t2.daemon=True
    t1.start()
    t2.start()

if __name__=='__main__':
    test()
