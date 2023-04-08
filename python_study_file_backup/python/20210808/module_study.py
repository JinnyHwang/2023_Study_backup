
import math

r = 10
print(2+math.pi*r)

#올림
print(math.ceil(2.5))

#내림
print(math.floor(2.5))


import random

candidates = ['가위', '바위', '보']

for i in range(5) :
    print(random.choice(candidates))


def get_web(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

#print(get_web('https://www.google.com/'))
#print(get_web('https://example.com/'))

import datetime

now = datetime.datetime.now()
print('현재 시각 {} : {}년 {}월 {}일 {}시 {}분 {}초'.format(now, now.year, now.month, now.day, now.hour, now.minute, now.second))

today_day = datetime.date.today()
print('오늘 날짜는 {}'.format(today_day))

next_day = 1
print('{}일 후 날짜는 {}'.format(next_day, today_day+datetime.timedelta(days=next_day)))


