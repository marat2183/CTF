from socket import *
Server_host = '51.158.165.206'
Server_port = 9091
socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.connect((Server_host, Server_port))
while True:
    data = socket_object.recv(1024).decode()
    data1 = data.strip()
    if 'KHCTF' in data1:
        print (data1)
        break
    else:
        data2 = data1.split('\n')
        print(data2[1])
        answer = data2[1].upper() + '\r\n'
        socket_object.sendall(answer.encode())
        print(answer)