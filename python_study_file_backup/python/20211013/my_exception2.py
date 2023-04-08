from UnexpectedRSPValue import UnexpectedRSPValue

#value = '가위'
value = '가'

try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("에러발생")
    


