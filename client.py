# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:01:01 2019

@author: melkhafef
"""
try:
    from socket import *
    s=socket(AF_INET,SOCK_STREAM)
    host="127.0.0.1"
    port=8000
    s.connect((host,port))
    while True :
        s.send((input("I:")).encode('utf-8'))
        x=s.recv(2048)
        print("server:",x.decode('utf-8'))
    s.close()
except error as e :
    print(e)
except KeyboardInterrupt :
    print('Ok')
    