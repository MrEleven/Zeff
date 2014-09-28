今天找了一个不错的网站http://www.nowamagic.net/librarys/veda/detail/2566，这是一个个人博客，里面的东西全部的都是一个人写的。这里有一系列专门讲python源码分析的。

今天本来想看tornado源码的，但是刚打开web.py这个文件的时候，发现了threading模块，现在对这个模块不是很熟，所以需要补课（陌聲人的说法）。

首先threading模块是thread模块的封装，Python用于操作线程的方法一共有两种，一种是通过函数start_new_thread()来返回一个线程对象。另外一种是利用threading模块中的Thread类。

下面这种是通过thread.start_new_thread()来创建线程的

import time
import thread

def hello(id):
i = 0
while i<=10:
print '%s say "hello!"' % id
i = i+1
time.sleep(1)

def test():
thread.start_new_thread(hello, ('A',))
thread.start_new_thread(hello, ('B',))

下面这种是通过threading.Thread来创建线程
import time
import thread

def hello(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.thread_stop = False
    def run(self):
        i = 0
        while i<=10:
            print '%s say "hello!"' % self.id
            i = i + 1
            time.sleep(1)

    def stop(self):
        self.thread_stop = True

def test():
    thread1 = hello('A')
    thread2 = hello('B')
    thread1.start()
    thread2.start()
    time.sleep(11)
    thread1.stop()
    thread2.stop()
    
python中的枷锁机制和C#中的大同小异。

通过acquire()函数获得锁，通过release()函数释放锁。threading模块中把Lock进行了优化，产生了RLock。RLock的好处就是确保一个进程只能对一个锁acquire()一次，从而保证不会进入死锁。

Condition是对RLock的再一次封装，Condition比较有意思的地方就是提供了wait和notify机制，

来个经典的生产者消费者代码，尽管我认为我的代码说明不了任何问题，但是我真心想不出什么来说明这个问题。


今天找了一个不错的网站http://www.nowamagic.net/librarys/veda/detail/2566，这是一个个人博客，里面的东西全部的都是一个人写的。这里有一系列专门讲python源码分析的。

今天本来想看tornado源码的，但是刚打开web.py这个文件的时候，发现了threading模块，现在对这个模块不是很熟，所以需要补课（陌聲人的说法）。

首先threading模块是thread模块的封装，Python用于操作线程的方法一共有两种，一种是通过函数start_new_thread()来返回一个线程对象。另外一种是利用threading模块中的Thread类。

下面这种是通过thread.start_new_thread()来创建线程的

import time
import thread

def hello(id):
i = 0
while i<=10:
print '%s say "hello!"' % id
i = i+1
time.sleep(1)

def test():
thread.start_new_thread(hello, ('A',))
thread.start_new_thread(hello, ('B',))

下面这种是通过threading.Thread来创建线程

import time
import thread

def hello(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.thread_stop = False
    def run(self):
        i = 0
        while i<=10:
            print '%s say "hello!"' % self.id
            i = i + 1
            time.sleep(1)

    def stop(self):
        self.thread_stop = True

def test():
    thread1 = hello('A')
    thread2 = hello('B')
    thread1.start()
    thread2.start()
    time.sleep(11)
    thread1.stop()
    thread2.stop()
    
python中的枷锁机制和C#中的大同小异。

通过acquire()函数获得锁，通过release()函数释放锁。threading模块中把Lock进行了优化，产生了RLock。RLock的好处就是确保一个进程只能对一个锁acquire()一次，从而保证不会进入死锁。

Condition是对RLock的再一次封装，Condition比较有意思的地方就是提供了wait和notify机制，

来个经典的生产者消费者代码，尽管我认为我的代码说明不了任何问题，但是我真心想不出什么来说明这个问题。

import threading
import time
import random

x=0
con = threading.Condition()

class Producer(threading.Thread):
    def __init__(self, t_name):
        threading.Thread.__init__(self, name=t_name)
    
    def run(self):
        global x
        while True:
            if x == 5:
                print 'the house is full, Producer is finished';
                break
            if x<5:
                con.acquire()
                x = x + 1
                con.notify()
                print "producing..." + str(x)
                con.release()
                time.sleep(random.randrange(5))


class Consumer(threading.Thread):
    def __init__(self, t_name):
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        global x
        while True:
            if x == 0:
                print 'the house is empty, Consumer is finished'
                break
            if x > 0:
                con.acquire()
                x = x - 1
                con.notify()
                con.release()
                print "consuming..." + str(x)
                time.sleep(random.randrange(5))


def test():
    c = Consumer("Consumer")
    d = Producer("Producer")

    d.start()
    c.start()
    
还有一个是队列。悲剧，睡觉时间到了，以后坚持早睡。晚安了，各位程序猿们。