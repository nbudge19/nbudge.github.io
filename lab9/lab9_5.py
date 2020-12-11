import threading,time,random

def timer(interval):
    for i in range(5):
        time.sleep(random.choice(range(interval)))
        thread_id=threading.get_ident()
        print("Tread:{0} Time:{1} \n".format(thread_id, time.ctime()))

def writefile(interval):
    f=open('abc.txt','a')
    for i in range(5):
        time.sleep(random.choice(range(interval)))
        thread_id=threading.get_ident()
        str1="Tread:{0} Time:{1} \n".format(thread_id, time.ctime())
        f.write(str1)
    f.close

def test():
    t1=threading.Thread(target=timer,args=(5,))
    t2=threading.Thread(target=writefile,args=(5,))
    t1.start()
    t2.start()

if __name__=='__main__':
    test()
    
