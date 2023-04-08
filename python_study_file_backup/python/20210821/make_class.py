
class Jieun():
    '''지은지은'''

jinjin = Jieun()
euneun = Jieun()

jinjin.a = '??'
euneun.a = '!!'

print(jinjin.a)
print(euneun.a)

jinjin.b = 'ㅇㅇ'
euneun.b = 'ㅁㅁ';

def speak(p):
    print('class test {}는 a {}는 b '.format(p.a, p.b))

#class에 func 추가
Jieun.speakA = speak

jinjin.speakA()
euneun.speakA()
