
n1 = 2554
print('?')
print(n1%(10**1))
print(n1%(10**2))
print(n1%(10**3))
print(n1%(10**4))
print('?')
print(n1//(10**1))
print(n1//(10**2))
print(n1//(10**3))
print(n1//(10**4))
print('??')
print(str(n1%(10**1))[0])
print(n1)
n1 += (10**1)
print(n1)
print(str(n1%(10**2))[0])
print(str(n1%(10**3))[0])
print(str(n1%(10**4))[0])

#print(len(str(n1)))

for i in range(4,-1,-1):
    print('??',i)

def solution(numbers):
    # 가장 큰 수
    # 맨 앞에 큰 수가 오도록
    # 앞자리가 같은 수면?
    # number원소는 최대 4자리. 각 원소를 반복해서 붙인다 가정. 가장 큰 수가 앞쪽으로

    # 1번째 자리 기준으로 배열 정렬
    #numbers.sort(key = lambda x : str(x)[0] , reverse=True)
    #print(numbers)

    numbers = [3, 30, 34, 3434, 5, 9]
    # 정렬용 dictionary 만들자 key = "4자리수문자열" , value = 배열인덱스
    numbers_dic = {}
    val2 = ''
    for ni, nv in enumerate(numbers):
        val2 = (str(nv)*4)[:4]
        numbers_dic[val2] = numbers_dic.get(val2, []) + [ni]
        #numbers_dic[val2] = ni
    print(numbers_dic)
    
    print(numbers_dic.get('3434'))

    numbers_dic_sort = {}
    numbers_dic_sort = sorted(numbers_dic, key = lambda x : (x[0], x[1], x[2], x[3]), reverse = True)
    #rint(numbers_dic_sort)
    #print('?',str(numbers_dic_sort[0])[0])
    if str(numbers_dic_sort[0])[0] == 0:
        return '0'
    
    answer = ''
    for nds in numbers_dic_sort:
        for nd in numbers_dic[nds]:
            answer += str(numbers[nd])
        #print('?',numbers_dic[nds])
        #answer += str(numbers[numbers_dic[nds]])
    #print(answer)
    
    return answer

print(solution([]))
