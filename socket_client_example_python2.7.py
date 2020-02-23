from socket import *
#import hashlib
Server_host = '51.158.165.206'
Server_port = 9091
socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.connect((Server_host, Server_port))
while True:
    data = socket_object.recv(1024).strip()
    if 'KHCTF' in data:
        print (data)
        break
    else:
        data1 = data.split('\n')
        print(data1[1])
        answer = data1[1].upper() + '\r\n'
        socket_object.sendall(answer)
        print(answer)