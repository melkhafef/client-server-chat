# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:48:33 2019

@author: melkhafef
"""

from socket import *
from threading import Thread
def server(session,ip,port):
    while True :
        client_message=session.recv(2048)
        print("client.{}.{}:".format(ip,port),client_message.decode('utf-8')) 
        session.send((input("server:")).encode('utf-8'))
try:
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    host="127.0.0.1"
    port=8000
    s.bind((host,port))
    s.listen(10)
    while True :
         session,addr=s.accept()
         ip=addr[0]
         port=addr[1]
         print("{}.{} join to chat".format(addr[0],addr[1]))
         Thread(target=server,args=(session,ip,port)).start()
    s.close()
except error as e :
    print(e)
except KeyboardInterrupt :
    print("Ok")

