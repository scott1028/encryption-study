# coding: utf-8

import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# 偽隨機數生成器
random_generator = Random.new().read
# rsa算法生成實例, 如果要實作 Wik 上的演算法要靠這邊取得 'n', 'e', 'd', 'p', 'q', 'u' 否則等產生 Private & Public Key 再取會缺少部份數值.
rsa = RSA.generate(1024, random_generator)

# master的秘鑰對的生成
private_pem = rsa.exportKey()

public_pem = rsa.publickey().exportKey()

print '-' * 40

print private_pem
print
print public_pem

print '-' * 40

# CONST
MSG = 'tested by scott'

# encryt by public_pem key testcase
key1 = RSA.importKey(public_pem)
cipher = PKCS1_OAEP.new(key1)
cipher_txt = cipher.encrypt(MSG)
print base64.b64encode(cipher_txt)

# decrypt by private_pem key testcase
key2 = RSA.importKey(private_pem)
cipher = PKCS1_OAEP.new(key2)
msg = cipher.decrypt(cipher_txt)
print msg

import pdb; pdb.set_trace()
