import datetime

hundred = datetime.timedelta(days = 100)
print(type(hundred))
print(hundred)

print(datetime.datetime.now())
print(datetime.datetime.now() + hundred)
print(datetime.datetime.now() - hundred)
hundred = datetime.timedelta(days = -100)
print(datetime.datetime.now() + hundred)
'''
2021-10-13 20:16:21.637743
2022-01-21 20:16:21.637743
2021-07-05 20:16:21.637743
2021-07-05 20:16:21.637743
'''