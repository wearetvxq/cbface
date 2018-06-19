# - * - coding: utf-8 - * -
import socket,time
import threading
import binascii
class IO:
    f = 0
    def __socke(self):
        # 创建套接字
        tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket---%s' % tcpClientSocket)
        # 链接服务器
        serverAddr = ('192.168.13.18', 50000)
        tcpClientSocket.connect(serverAddr)
        print('connect success!')
        return tcpClientSocket

    #开门方法
    def open(self, num):
        try:
            data = code = ''
            if num == 0:
                code = 'CCDDA101FFFFFFFF9E3C'
            elif num == 1:
                code = 'CCDDA10100010001A448'
            elif num == 2:
                code = 'CCDDA10100020002A64C'
            elif num == 3:
                code = 'CCDDA10100040004AA54'
            elif num == 4:
                code = 'CCDDA10100080008B264'
            elif num == 5:
                code = 'CCDDA10100100010C284'
            elif num == 6:
                code = 'CCDDA10100200020E2C4'
            elif num == 7:
                code = 'CCDDA101004000402244'
            elif num == 8:
                code = 'CCDDA10100800080A244'
            sock = self.__socke()
            sock.send(binascii.a2b_qp(code))
            data = sock.recv(1024)
            sock.close()
            print(data)
            if data.decode('utf-8') == 'OK!':
                return True
            else:
                return True
        except:
            return True

    #关门方法
    def close(self, num):
        try:
            data = code = ''
            if num == 0:
                code = 'CCDDA1010000FFFFA040'
            elif num == 1:
                code = 'CCDDA10100000001A346'
            elif num == 2:
                code = 'CCDDA10100000002A448'
            elif num == 3:
                code = 'CCDDA10100000004A64C'
            elif num == 4:
                code = 'CCDDA10100000008AA54'
            elif num == 5:
                code = 'CCDDA10100000010B264'
            elif num == 6:
                code = 'CCDDA10100000020C254'
            elif num == 7:
                code = 'CCDDA10100000040E2C4'
            elif num == 8:
                code = 'CCDDA101000000802244'
            sock = self.__socke()
            sock.send(binascii.a2b_qp(code))
            data = sock.recv(1024)
            sock.close()
            if data.decode('utf-8') == 'OK!':
                return True
            else:
                return True
        except:
            return True

if __name__ == '__main__':
    a = IO()
    #a.open(0)
    #a.close(8)