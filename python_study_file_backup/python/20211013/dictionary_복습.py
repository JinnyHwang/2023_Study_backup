
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic2 = {}

print( list( dic.keys() ) )
print( list( dic.values() ) )
print( list( dic.items() ) )

# key로 탐색하는 get
print( dic.get('name') )

# 없는 key일 때 default로 return 할 값을 정함.
#print( dic.get('empty', 'default') )
dic2['empty'] = dic.get('empty', 'default')
print(dic2['empty'])
print(dic2)

