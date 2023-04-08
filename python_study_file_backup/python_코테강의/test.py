def solution(number, k):
    # 큰수를 만들기위해서는 맨 앞에 가장 큰 수가 나와야한다
    # 맨 앞에서부터 비교
    # 다음에 들어올 숫자가 더 크다면
    # 이전에 들어온 앞숫자 빼기 pop
    # 내 앞 숫자가 더 크다면 현재수 더하기 append
    # 뺄 수 있는 횟수를 소진하면 리스트에 남은 숫자 ++
    # 탐색이 끝났는데 k가 남아있는 경우
    # 맨 뒷자리에서부터 뺀다
    
    # 빈 리스트 생성
    result = []
    
    # 문자열 인덱스 하나하나 탐색
    # enumerate를 사용하면 인덱스도 함께 확인 가능
#    for num in number :
    for i, num in enumerate(number):
       # 다른 조건문에서 해당 동작 대체
       # if len(result)==0:
       #     result.append(num)
        
        # 탐색하는 숫자가 result의 마지막 숫자보다 작을 때까지 제거 반복
        while len(result) > 0 and result[-1] < num and k > 0:
            result.pop()
            k -= 1
        if k == 0:
            result.append(number[i:])
            break
        result.append(num)
    
    # 아직 뺄 횟수가 남아있음
    # 맨 뒤에서부터 k개수만큼 자름
    if k > 0:
        result = result[:-k]
        
    print(result)
    
    # 현재 리스트형태로 구성
    # 문자열 형태로 반환
    answer = ''.join(result)
    return answer


print(solution("1924", 2))
