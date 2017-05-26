# 非對稱式加密運作方式

- 必看 Ref: https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29
- Ref: https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95
- Ref: https://pythonhosted.org/pycrypto/
- 關於 Mod 公式轉換 Ref: https://zh.wikipedia.org/wiki/%E6%A8%A1%E5%8F%8D%E5%85%83%E7%B4%A0

```
Encrypt formula: c = (n^e) mod n
Decript formula: c^d = ( n^(e-d) ) mod n
```

```
A-Key encrypts message to cipher -> B-Key decrypts cipher to message.
	... or
B-Key encrypts message to cipher -> A-Key decrypts cipher to message.
P.S 但大部份實作 Private Key 不會作為加密使用!
```

- ![Alt text](https://raw.githubusercontent.com/scott1028/encryption-study/master/sample01_rsa.png "sample01_rsa.png")
- ![Alt text](https://raw.githubusercontent.com/scott1028/encryption-study/master/sample01_lib.png "sample01_lib.png")
- ![Alt text](https://raw.githubusercontent.com/scott1028/encryption-study/master/sample02_rsa.png "sample02_rsa.png")
