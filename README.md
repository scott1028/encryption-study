# 非對稱式加密運作方式

- Ref: https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95

```
Encrypt formula: c = (n^e) mod n
Decript formula: c^d = ( n^(e-d) ) mod n
```

```
A-Key encrypts message to chipher -> B-Key decrypts chipher to message.
	... or
B-Key encrypts message to chipher -> A-Key decrypts chipher to message.
```
