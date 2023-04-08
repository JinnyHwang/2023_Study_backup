# https://m.blog.naver.com/PostView.nhn?blogId=qbxlvnf11&logNo=221434003885&proxyReferer=https:%2F%2Fwww.google.com%2F
# list 안에 for문
# [ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]
# if문 쓸 수 있고, for문 여러개 가능

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1_1 = [ num*3 for num in list1 ]
print(list1_1)

list1_2 = [ num*3 for num in list1 if num%2 == 1 ]
print(list1_2)

list1_3 = [ num*num2 for num in list1 if num%2 == 1
            for num2 in list1 if num2%2 == 1]
print(list1_3)
