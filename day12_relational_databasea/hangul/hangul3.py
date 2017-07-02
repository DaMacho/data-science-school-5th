# -*- coding: utf-8 -*-
a = '한글'

b = a.decode('utf-8')
print b
print type(b)

c = b.encode('euc-kr')
print c
print type(c)
