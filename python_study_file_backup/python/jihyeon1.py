#2018.11.25
#18101899
#안경광학과
#황지현

#math 라이브러리 import
import math

#실행시킬 내용을 담고 있는 함수
def input_bmi():
    #kg, cm, bmi변수 사용
    kg = float(input("무게(킬로그램): "))
    cm = float(input("키(미터): "))
    bmi = kg/pow(cm, 2)
    print("당신의 BMI: ", bmi);
    return bmi

def result_bmi(bmi):
    if 20 <= bmi and bmi < 25 :
        print("정상입니다.")
    elif 25 <= bmi and bmi < 30 :
        print("과체중입니다.")
    elif 30<= bmi :
        print("비만입니다.")
    return


result_bmi(input_bmi())
