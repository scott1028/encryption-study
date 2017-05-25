#!/usr/bin/python
# -*- coding: utf8 -*-

# Simple RSA Implementation
# Authored by Jeremy <jeremy5189(at)gmail.com>
# Reference: http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html

from fractions import gcd
import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# 選擇兩個質數以及欲加密的明文(int only)
p = 61
q = 53
messsage = 2014

# 乘積
n = p * q

# 檢查明文長度
if len(str(n)) < len(str(messsage)):
	raise Exception('message(' + str(len(str(messsage))) + \
		') 不能比 n(' + str(len(str(n))) + ') 還要長')

# 計算n的歐拉函數 φ(n)
# φ(n) = (p-1)(q-1)
phi = (p - 1) * (q - 1)

# 隨機選擇一個整數 e
# 1 < e < φ(n) AND gcd( e, φ(n) ) = 1
e = 0
for i in xrange( 2, phi ):
	if gcd( i, phi ) == 1:
		e = i
		break

# 計算 e 對於 φ(n) 的模反元素 d
# e * d mod φ(n) = 1

# 相當于二元一次方程式 ( 令 d 為 x, y 為除式之商, e, φ(n) 為常數  )
# e * x + φ(n) * y = 1

# 欲此方程式，需利用「擴展歐幾里得演算法」
# 即：給予二整數 a 、b, 必存在有整數 x 、 y 使得 ax + by = gcd(a,b)
# 今 a = e, b = φ(n) 且 gcd( e, φ(n) ) = 1
# 故符合 e * x + φ(n) * y = 1
d = modinv( e, phi );

# 金鑰產生完成，準備加密資料
# 待加密的資料只能為數字
plain = messsage

# 使用公鑰 (n,e) 加密
# pow( x, y, z ) = x^y % z
# m^e ≡ c (mod n)
cipher = pow( plain, e, n ) 

# 使用私鑰 (n,d) 解密
# c^d ≡ m (mod n)
decrypted = pow( cipher, d, n)

# 印出整個過程
print "--------- Variables ---------"
print "* p = " + str(p)
print "* q = " + str(q)
print "* n = " + str(n)
print "* phi = " + str(phi)
print "* e = " + str(e)
print "* d = " + str(d)
print "----------- Keys ------------"
print "* Public (n,e) = (" + str(n) + "," + str(e) + ")"
print "* Private (n,d) = (" + str(n) + "," + str(d) + ")"
print "* N Bit = " + str(len(bin(n)))
print "---------- Messages ---------"
print "* Plain: " + str(plain)
print "* Encrypted: " + str(cipher)
if plain == decrypted:
	print "* Decrypted: " + str(decrypted) + " (Correct)"
else:
	print "* Decrypted: " + str(decrypted) + " (Failed)"
print "----------- End -------------"

# Ref: https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95
# Ref: http://www.kaiching.org/2011/02/python-pow.html
# 測試驗證 使用 "私鑰" 加密 "公鑰" 解密
# 他使用起先與Alice約好的格式將 m 轉換為一個小於 N，且與 N 互質的整數 n，比如他可以將每一個字轉換為這個字的 Unicode 碼，然後將這些數字連在一起組成一個數字。
# Python: pow(x, y[, z]) -> 回傳 xy 之值，或是 xy % z 之值

print

message = 1028
c = pow( message, d, n)
p = pow( c,  e, n )

print d, e, n
print '測試驗證 使用 "私鑰" 加密 "公鑰" 解密 ->'
print '>> 輸入:', message, '由私鑰加密產生密文: ', c, '由密文用公鑰解密:', p
