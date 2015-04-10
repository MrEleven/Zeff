#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2015-04-10
# Author : Mr.Eleven
# Email  : iGod_eleven@163.com

"""
    a simple echo server using select
"""

# server.py
import select
import socket
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 10001)
server.bind(server_address)
server.listen(10)

inputs = [server]
outputs = []
message_queues = {}

timeout = 20

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
    if not (readable or writable or exceptional):
        print "Time out !"
        break;
    for s in readable:
        # 如果又客户端连接服务器
        if s is server:
            connection, client_address = s.accept()
            print "get a connect", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        # 如果套接字不是server，那么说明是已经建立了连接的普通通信
        else:
            data = s.recv(1024)
            if data:
#                print " received ", data, " from ", s.getpeername()
                print " receive ", data
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print "  closing", client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
#            print "  ", s.getpeername(), "queue empty"
            outputs.remove(s)
        else:
            print " sending ", next_msg #, " to ", s.getpeername()
            s.send(next_msg)
            
    for s in exceptional:
#        print " exception condition on ", s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
            s.close()
            del message_queues[s]


# client.py
import socket

messages = ["Tomorrow, so happy", "Watch <<Fast & Furious>>", "The important with beauty"]
server_address = ("127.0.0.1", 10001)
socks = []

for i in range(2):
    socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

for s in socks:
    s.connect(server_address)

counter = 0
for message in messages:
    for s in socks:
        counter += 1
        s.send(message)
#        s.send(message + " version " + str(counter))
    for s in socks:
        data = s.recv(1024)
        if not data:
            s.close()
            print 'closed', s.getpeername()


# 其实最关键的还是理解文件描述符是个神马东西，不然很难入门。
