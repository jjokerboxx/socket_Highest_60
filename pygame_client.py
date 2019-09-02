#-*- coding: utf-8 -*-

from socket import *
import threading
import time

# cd desktop
# cd Highest_60
# python pygame_client.py


print("Recv Start!")
clientSock = socket(AF_INET, SOCK_STREAM)  #create socket object
print('socket created')

clientSock.connect(('127.0.0.1', 8080))  #beware the input is 'tuple' address


def send(sock):
    while True:
        cl_msg = input("send : ")
        sock.send(cl_msg.encode('utf-8'))

def receive(sock):
    while True:
        rcv = clientSock.recv(2048)
        print(rcv.decode('utf-8'))

sender = threading.Thread(target=send, args=(clientSock,))  # Tread get target func name and it's param as an argument
receiver = threading.Thread(target=receive, args=(clientSock,)) # Also beware that args should be an iterable data, so there's only one variable in tuple or something iterable, it should contain 'comma' in the parentheses
 
sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass


# msg = clientSock.recv(2048)
# print(msg.decode('utf-8'))

# # 숫자 입력
# cl_num = str(input("my number is = "))
# clientSock.send(cl_num)

# # 결과 받기
# rst = clientSock.recv(2048)
# print(rst.decode('utf-8'))
