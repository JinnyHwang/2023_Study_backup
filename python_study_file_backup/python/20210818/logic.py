a = 10
if a<0 and 2**a>1000 and a%5==2 and round(a)==a :
    print('아이고 구분 힘들어')

def return_false():
    print('함수 return_false')
    return False

def return_true():
    print('함수 return_true')
    return True

print('test1')
a = return_false()
b = return_true()

if a and b:
#if return_false() and return_true():
    print(True)
else:
    print(False)

dic = {'Key2':'Value1'}
#if 'Key1' in dic and dic['Key1']=='Value1':
if dic['Key1']=='Value1' and'Key1' in dic : #단락평가
    print('yep')
else:
    print('nope')


