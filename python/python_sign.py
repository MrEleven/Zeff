import os, signal, time

def onsignal_init(a, b):
    print 'get init message'

signal.signal(signal.SIGINT, onsignal_init)

while True:
    time.sleep(10)


# 信号可以产生软件终端，python标准库中signal模块就是为信号而诞生的。
# Ctrl-C发送的信号是SIGINT。
# 可以用在八爪鱼中，获取一个结束信号之后可以让没有完成的任务完成了再结束。
