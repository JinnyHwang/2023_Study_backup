'''
hundred_after가 지금으로부터 100일 후, 9시 정각을 값으로 가지는
datetime클래스의 인스턴스가 되도록 만들어 보세요.
(단, 정각의 기준은 초 단위까지만 맞으면 됩니다.)
'''

import datetime

hundred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days = 100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))