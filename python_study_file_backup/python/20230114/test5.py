def solution(number, k):
    
    #number = "1924"
    #k = 2
    
    #number = "1231234"
    #k = 3
    
    number = "4177252841"
    k = 4

    # k번 제거할 수 찾기
    # 제거 우선순위는? 어렵따...
    # 앞자리에 큰 수가 오도록.. 어케하지..

    # 맨 앞에서부터 index확인
    # 만약 다음 숫자보다 값이 작으면 삭제
    # 만약 다음 숫자보다 값이 크면 패쓰
    del_index = [ -1 for _ in range(k) ]
    print(del_index)
    cnt_k = 0

    # 맨 마지막 자리수를 빼는 경우
    # 한 번에 안끝나는 경우
    
    first_num_i = [int(number[0]),0]
    first_num_com = []

    for i in range(len(number)):
        print('\n i? ', i, ' number[i]? ', number[i], ' cnt_k? ', cnt_k, ' del_index? ', del_index)
        if cnt_k == k:
            break

        if i < len(number)-1 and int(number[i]) < int(number[i+1]):
            del_index[cnt_k] = i
            cnt_k += 1
        else:
            if i != 0 and first_num_i[0] > int(number[i]):
                first_num_com.append([int(number[i]), i])
            
            elif first_num_i[0] < int(number[i]):
                #del_index[cnt_k] = first_num_i[1]
                #cnt_k += 1
                first_num_com.append(first_num_i)
                first_num_i = [int(number[i]), i]
            
            print('first_num_com? ',first_num_com)
            
            if i == len(number)-1:
                break
                
    print(del_index)
    print(first_num_com)
    first_num_com.sort()
    print(first_num_com)
    print('cnt_k? ',cnt_k)
    
    first_num_com_i = 0
    if cnt_k < k:
        for i in range(cnt_k, k):
            #print('??', i)
            #print(del_index[i])
            #print(first_num_com[first_num_com_i])
            del_index[i] = first_num_com[first_num_com_i][1]
            first_num_com_i += 1
    print(del_index)


    answer = ''
    return answer

print(solution("", 0))
