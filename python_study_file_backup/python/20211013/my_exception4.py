# 이 아래에 Exception을 상속 받는 MyException클래스를 정의하세요.

# Exception 클래스를 상속받은 MyException 클래스
class MyException(Exception):
    '''예외처리 클래스 정의'''

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

for name, products in shops.items():
    for product, price in products.items():
        if price == 3000:
            print("{} 가격은 {}".format(product, price))



try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException #새로 정의한 exception
except MyException: #에러 발생시 하는 동작
    print("풀을 찾았습니다.")