#-*- coding: utf-8 -*-

# import random as rd
import time
import threading
from socket import *


# cd desktop
# cd Highest_60
# python pygame_server.py


# highest 60 game with socket 
print("Game Start!")

serverSock = socket(AF_INET, SOCK_STREAM) # AF_INET -> IPv4, INET6 -> IPv6  ||  SOCK_STREAM -> TCP, SOCK_DGRAM -> UDP, SOCK_RAW -> packet
print('socket created')

serverSock.bind(('', 8080))  #beware the input is 'tuple' address
serverSock.listen(1)  #only one connection allowed
connSock, addr = serverSock.accept()



def sending(sock):
    while True:
        sv_msg = input("send : ")
        sock.send(sv_msg.encode('utf-8'))

def receive(sock):
    while True:
        rcv = connSock.recv(2048)
        print(rcv.decode('utf-8'))

# create Thread object
sender = threading.Thread(target=sending, args=(connSock,))  # Tread get target func name and it's param as an argument
receiver = threading.Thread(target=receive, args=(connSock,)) # Also beware that args should be an iterable data, so there's only one variable in tuple or something iterable, it should contain 'comma' in the parentheses
 
sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass


# # 통신 구동
# print("connection : ", str(addr))

# intro_msg = "The game started, choose your number in range 1 ~ 60"

# connSock.send(intro_msg.encode('utf-8'))

# my_num = str(input("SVR choose : "))

# cl_num = connSock.recv(2048)

# print("client choose : ", cl_num)

# # 결과 출력
# result_W = "You Win"
# result_L = "You Lose"
# result_D = "DRAW"

# # 받은 데이터를 정수로 변환
# my_num = int(my_num)
# cl_num = int(cl_num)


# # 게임 룰  ||  중복되는 부분을 파이썬스럽게 바꿀 수는 없을까?
# if my_num > cl_num:
#     a = my_num - cl_num
#     b = 60 - my_num
#     if a > b:
#         print("client WIN!!!")
#         connSock.send(result_W.encode('utf-8'))
        
#     else:
#         print("server WIN!!!")
#         connSock.send(result_L.encode('utf-8'))

# elif my_num == cl_num:
#     print("DRAW!!!")
#     connSock.send(result_D.encode('utf-8'))
# elif my_num < cl_num:
#     a = cl_num - my_num
#     b = 60 - cl_num
#     if a > b:
#         print("client WIN!!!")
#         connSock.send(result_W.encode('utf-8'))
#     else:
#         print("server WIN!!!")
#         connSock.send(result_L.encode('utf-8'))
# else:
#     print("Something went worng")