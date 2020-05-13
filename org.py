import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import new as Random
import random
from base64 import b64encode
from base64 import b64decode


def power(a, n, m):
    res = 1
    p = a % m
    while n:
        if (n & 1):
            res = (res * p) % m
        n >>= 1
        p = (p * p) % m
    return res


print("9")
key = RSA.generate(1024)
print('n = ',key.n)
print('e = ',key.e)
print('d = ',key.d)
price = random.randint(500000,100000000)
print( 'Price is', price)
sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
connA, addrA = sock.accept()
connB, addrB = sock.accept()
print('n',key.n)
n = (str(key.n)+' ').encode()
e = (str(key.e)+' ').encode()
price_en = (str(price)).encode()
data = (str(key.n)+' '+str(key.e)+' '+str(price)).encode()

connA.send(data)
#connA.send(e)
#connA.send(price_en)

en_priceA = int(connA.recv(512).decode())
print('Encrypt_price 1: ', en_priceA)

connB.send(data)
#connB.send(e)
#connB.send(price_en)

en_priceB = int(connB.recv(512).decode())
print('Encrypt_price 2: ', en_priceB)

priceA = power(en_priceA,key.d,key.n)

priceB = power(en_priceB,key.d,key.n)

print('priceA = ',priceA)
print('priceB = ',priceB)

print('max price is ',max(priceA,priceB))
connA.close()
connB.close()


