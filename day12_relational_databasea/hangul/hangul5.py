# -*- coding: utf-8 -*-

# str, unicode 함수 호출 시, 기본 인코딩 변경
import sys
reload(sys)
sys.setdefaultencoding('euc-kr')

import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.khan.co.kr/', allow_redirects=False)
soup = BeautifulSoup(res.content, 'html5lib', from_encoding='euc-kr')

# 기본 euc-kr로 변경하도록 함
print str(soup.title.get_text())

b = str(soup.title.get_text())
print unicode(b)
