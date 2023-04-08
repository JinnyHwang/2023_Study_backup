#value = '가위'
value = '가'

try:
    if value not in ['가위', '바위', '보']:
        raise ValueError("가위바위보 중 하나 내야함") #에러 발
except ValueError:
    print("에러발생")
    
#파이썬에서는 예외도 클래스
#새로운 예외 만들기 쉬움

