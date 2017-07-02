# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.khan.co.kr/', allow_redirects=False)
soup = BeautifulSoup(res.content, 'html5lib', from_encoding='euc-kr')

# Windows의 경우 화면 출력에는 아래와 같이 함
# 매번 인코딩 디코딩을 해야 한다면 귀찮은 작업임
print soup.title.get_text().encode('euc-kr')

# 기본적으로 str로 변환 시, ascii라고 가정
print str(soup.title.get_text())

# 단 DB에 저장하거나 네트워크 전송을 할 때는
# 해당 DB의 스키마나 전송 받는 곳의 규약에 따라 전달
# 일반적으로 utf-8이 가장 많이 사용 됨
soup.title.get_text().encode('utf-8')

