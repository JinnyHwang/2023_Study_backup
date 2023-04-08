
s = {1,2,3,4}
print(type(s))
print(type(sorted(s)))
print(type(s.sort()))

l1 = [2, 3, 5, 4, 9, 7, 1]
print(l1)
print(l1[-1]) # 맨 끝자리 숫자를 의미
print(l1[:-1]) # 맨 끝자리 숫자 직전까지
print(l1[-2]) # 끝에서 2번째 숫자를 의미
print(l1[:-2]) # 끝에서 2번째 숫자 직전까지

s1 = '256741'
print(list(s1))

col = ['3','5']

col.extend(list(s1[:2]))
print(col)

