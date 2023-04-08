import datetime

# datatime class에는 now() 메서드가 있음
print ( datetime.datetime.now() )

start_time = datetime.datetime.now()
# 2021-10-13 20:09:26.917552

print( type(start_time) )
# <class 'datetime.datetime'>

start_time = start_time.replace(year=2020, month=2, day=1)
print(start_time)
# 2020-02-01 20:09:26.917552

start_time = datetime.datetime(2019,3,5)
print(start_time)
# 2019-03-05 00:00:00

how_long = datetime.datetime.now() - start_time
type(how_long)
print(how_long.days)
print(how_long.seconds)

