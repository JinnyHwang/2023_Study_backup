class BadUserName(Exception):
    ''''''
    
class PasswordNotMatched(Exception):
    ''''''

def sign_up():
    '''회원가입 함수'''

#내가 만든 함수 내가 걸고 싶은 예외처리
try:
    sign_up()
    name = '지은'
    pw = '0000'
    if name is not '지은':
        raise BadUserName
    if pw is not '1234':
        raise PasswordNotMatched
except BadUserName:
    print("이름 쓸 수 없음")
except PasswordNotMatched:
    print("비번 안똑같음")
