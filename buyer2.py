import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import new as Random
from base64 import b64encode
from base64 import b64decode
import random


def power(a, n, m):
    res = 1
    p = a % m
    while n:
        if (n & 1):
            res = (res * p) % m
        n >>= 1
        p = (p * p) % m
    return res
	
sock = socket.socket()
sock.connect(('localhost', 9090))
data = sock.recv(1024).decode()

index = data.find(' ')
n = int(data[0:index])
print('n = ',n)

index2 = data.find(' ',index+1)
e = int(data[index+1:index2])
print('e = ',e)

price = int(data[index2+1:])
print( 'Price is  ', price)
offer = random.randint(1,price)
print('Price bayer b: ', offer)
encr = power(offer,e,n)
#encr = rsa.encrypt(offer,key)
print('Price_en bayer b: ',encr)
sock.send(str(encr).encode())