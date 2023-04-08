
num1 = 5
num2 = 5.00

num3 = 5*1
num4 = 5*0.1

num5 = 6/5
num6 = 6//5

print('num1 : {} num2 : {} \nnum3 : {} num4 : {} \nnum5 : {} num6 : {}  '.format(num1, num2, num3, num4, num5, num6))

print(0.1+0.1)
print(0.1+0.1 == 0.2)

print(0.1+0.1+0.1)
print(0.1+0.1+0.1 == 0.3)

# 부동소수점 : 실수표현방식. 값을 정확히 표현할 수 없음
# 정수 영역은 정확함

print(int(5.0)) # 정수
print(float(5)) # 부동소수점
print(5*1.0) # 부동소수점

# https://dojang.io/mod/page/view.php?id=2466

# 실수는 유한한 비트로 표현하기 때문에 무한히 많은 실수를 정확하게 표현할 수 없음
# 유한한 비트를 사용해서 근삿값으로 실수를 표현함.
# 0.30000000000000004 값은 0.3을 표현한 근삿값이다.
# 부동소수점 반올림 오차(rounding error)
# 때문에 실수 판단시 == 를 사용하면 안된다.
# 위와 같은 이유로 0.1+0.2 != 0.3 이기 때문

# 머신 앱실론 : sys.float_info.epsilon에 저장된 값
# 머신 앱실론은 반올림오차의 상한값

# 특정 실수를 가장 가까운 부동소수점 실수로 반올림했을 때
# 상대 오차는 항상 머신 앱실론 이하이다
# 때문에 연산한 값과 비교할 값의 차이가 머신 앱실론보다 작거나 같으면
# 두 실수는 같은 값이라 할 수 있다.

# 때문에 math.fabs()를 사용해  두 값의 차이를 절대값으로 만들면
# 결과값이 음수여도 판단 가능
import math, sys
x = 0.1 + 0.2
re1 = math.fabs(x-0.3) <= sys.float_info.epsilon
print(re1) # True

# 파이썬 3.5 이상부터는 두 실수가 같은지 판단하기 위해 math.isclose() 사용
re2 = math.isclose(0.1+0.2, 0.3)
print(re2) # True

# Decimal로 정확한 자릿수표현
# 반올림 오차가 없는 고정소수점을 사용할 수 있음
# decimal은 숫자를 10진수로 처리
# 정확한 소수점 자릿수를 표현할 수 있다
from decimal import Decimal
re3 = Decimal('0.1') + Decimal('0.2')
re4 = Decimal('0.3')
print(re3, re4, re3 == re4) # 0.3 0.3 True

# 그러나 순환소수는 고정소수점으로도 정확하게 표현할 수 없음
# fractions를 사용해 분수로 표현
from fractions import Fraction
re5 = Fraction('10/3') # 3.3333.. 순환소수를 분수로 표현해줌
re6 = Fraction(10,3)
print(re5, re6) # 10/3 10/3




