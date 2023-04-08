'''
print(ord('C')+1)  # 68
print(chr(ord('C')+1)) # D
print(str(ord('C')+1)) # 68
#print('C'+chr(1))

print( ord('A'), ord('Z'),ord('a'), ord('z') )

num = ord('A')
num = ord('Z')+1
if num > ord('Z') :
    num -= (ord('Z')-ord('A')+1)
    
print(num, chr(num))
    
    
# ord('A') <=   <=  ord('Z')
'''

def solution1(name):
    
    A_ascii = ord('A')
    Z_ascii = ord('Z')
    
    print( A_ascii, Z_ascii, chr(A_ascii+12), chr(Z_ascii-12), ord('M'), ord('N'))
    print(Z_ascii-ord('N'))
    
    name_ascii = [ ord(n)-A_ascii if ord(n) <= A_ascii+12 else Z_ascii-ord(n)+1 for n in name ]
    name_ascii_1 = [ ord(n)-A_ascii for n in name]
    
    print(name_ascii)
    print(name_ascii_1)
    
    for i in range(len(name_ascii)):
        print( chr( name_ascii[i] + A_ascii ),end='' )
    print('\n') 
    for i in range(len(name_ascii)):
        print( chr( Z_ascii-name_ascii[i]+1),end='' )
        
    print('\n')
    for i in range(len(name_ascii)):
        print( chr( name_ascii_1[i] + A_ascii ),end='' )
    print('\n')
    
    print(sum(name_ascii))
    
    
    
    #대문자만 사용    
    
    answer = 0
    return answer


def solution2(name):
    
    A_ascii = ord('A')
    Z_ascii = ord('Z')
    
    # 알파벳 커서 상하 이동횟수 구하기
    name_ascii = [ ord(n)-A_ascii if ord(n) <= A_ascii+12 else Z_ascii-ord(n)+1 for n in name ]
    
    print(name_ascii)
    
    answer = sum(name_ascii)
    
    # 커서 좌우 이동횟수 구하기 : 커서위치 index 0번째 좌우로 0이 있는지 확인
    if name_ascii[1] == 0 :
        print("???")
        for i in range(2, len(name_ascii)):
            if name_ascii[i] != 0:
                print(i)
                answer += (len(name_ascii) - i)
                return answer
        else: # 커서 이동이 필요 없는 경우
            return answer
    elif name_ascii[-1] == 0 :
        print("!!!", len(name_ascii))
        for i in range(len(name_ascii)-2, 1, -1):
            print(i, name_ascii[i])
            if name_ascii[i] != 0:
                answer += i
                return answer
        else: # 커서 이동이 필요 없는 경우
            return answer
    else :
        print("@@@")
        answer += (len(name) - 1)
        
    return answer


def solution3(name):
    
    A_ascii = ord('A')
    Z_ascii = ord('Z')
    
    # 알파벳 커서 상하 이동횟수 구하기
    name_ascii = [ ord(n)-A_ascii if ord(n) <= A_ascii+12 else Z_ascii-ord(n)+1 for n in name ]
    
    print(name_ascii)
    
    answer = sum(name_ascii)
    
    # 커서 좌우 이동횟수 구하기
    if 0 in name_ascii:
        i_0 = name_ascii.index(0)
        print('zero',i_0)
        
        zero_check = []
        # start index, 길이
        zero_check.append([i_0, 0])
        start = 0
        z_i = i_0
        z_m = 0
        # A가 연속되는 구간 구하기
        for i in range(i_0+1, len(name_ascii)):
            if name_ascii[i] == 0:
                if zero_check[start][0] == -1:
                    zero_check[start][0] = i
                else:
                    zero_check[start][1] += 1
                    if z_m < zero_check[start][1]:
                        z_i = zero_check[start][0]
                        z_m = zero_check[start][1]
            else :
                start += 1
                zero_check.append([-1,0])
        
        # zero_check[n][0] != -1 인 것 pass, zero_check[n][1] == 0 인것 연속X
        print("zero_check:",zero_check)
        
        print('z_i:{}  z_m:{}'.format(z_i, z_m))
        
        # A가 연속되는 구간 길이 확인.
        # 갔다가 되돌아오는 길이 vs 그냥 쭉 지나쳐서 가는 길이
        
        # 되돌아갔다 오는 길이
        # 0, len(name)-1,  z_i, z_m
        # 1. 0 ~ z_i 길이 vs z_i ~ len(name)-1
        # 앞쪽부터가 더 짧거나, 길이가 같은 경우
        # A가 연속되는 구간 직전까지 움직여야하는 커서를 확인
        print("1:{}, 2:{}".format(z_i-1, len(name) -z_i - z_m-1))
        # 짧은 쪽으로 먼저 움직였다 돌아오기
        c = 0
        # count하지 않았던 맨 앞자리를 탐색해야하기 때
        
        if z_i-1 <= len(name)-1 -z_i -z_m :
            c += 2*(z_i-1) + (len(name)-1 -z_i -z_m)
        else :
            c += 2*(len(name)-1 -z_i -z_m) + (z_i-1)
        
        if c < (len(name) - 1):
            answer += c
        else :
            answer += (len(name) - 1)
        return answer
            
    # A가 없는 경우 바로 답 return
    else :
        answer += (len(name) - 1)
        return answer
    
  #  check_zero = []
    
  #  for i, n in name_ascii:
  #      if n == 0:
            
    
    
    # 커서 좌우 이동횟수 구하기 : 커서위치 index 0번째 좌우로 0이 있는지 확인
    if name_ascii[1] == 0 :
        print("???")
        for i in range(2, len(name_ascii)):
            if name_ascii[i] != 0:
                print(i)
                answer += (len(name_ascii) - i)
                return answer
        else: # 커서 이동이 필요 없는 경우
            return answer
    elif name_ascii[-1] == 0 :
        print("!!!", len(name_ascii))
        for i in range(len(name_ascii)-2, 1, -1):
            print(i, name_ascii[i])
            if name_ascii[i] != 0:
                answer += i
                return answer
        else: # 커서 이동이 필요 없는 경우
            return answer
    else :
        print("@@@")
        answer += (len(name) - 1)
        
    return answer


def solution(name):
    
    A_ascii = ord('A')
    Z_ascii = ord('Z')
    
    # 알파벳 커서 상하 이동횟수 구하기
    name_ascii = [ ord(n)-A_ascii if ord(n) <= A_ascii+12 else Z_ascii-ord(n)+1 for n in name ]
    
    answer = sum(name_ascii)
    
    # 커서 좌우 이동횟수 구하기
    if 0 in name_ascii:
        i_0 = name_ascii.index(0)
        
        # [start index, 길이]
        zero_check = []
        zero_check.append([i_0, 0])
        start = 0
        z_i = i_0
        z_m = 0
        
        # A가 연속되는 구간 구하기
        for i in range(i_0+1, len(name_ascii)):
            if name_ascii[i] == 0:
                if zero_check[start][0] == -1:
                    zero_check[start][0] = i
                else:
                    zero_check[start][1] += 1
                    if z_m < zero_check[start][1]:
                        z_i = zero_check[start][0]
                        z_m = zero_check[start][1]
            else :
                start += 1
                zero_check.append([-1,0])
        
        # A가 연속되는 구간 길이 확인.
        # 갔다가 되돌아오는 길이 vs 그냥 쭉 지나쳐서 가는 길이
        # 1. 0 ~ z_i 길이 vs z_i ~ len(name)-1 길이
        # 앞쪽부터가 더 짧거나, 길이가 같은 경우
        # A가 연속되는 구간 직전까지 움직여야하는 커서를 확인
        print("1:{}, 2:{}".format(z_i-1, len(name) -z_i - z_m-1))
        # 짧은 쪽으로 먼저 움직였다 돌아오기
        c = 0
        # count하지 않았던 맨 앞자리를 탐색해야하기 때
        if z_i-1 <= len(name)-1 -z_i -z_m :
            c += 2*(z_i-1) + (len(name)-1 -z_i -z_m)
        else :
            c += 2*(len(name)-1 -z_i -z_m) + (z_i-1)
        
        if c < (len(name) - 1):
            answer += c
        else :
            answer += (len(name) - 1)
        return answer
            
    # A가 없는 경우 바로 답 return
    else :
        answer += (len(name) - 1)
        return answer
   


#print(solution("JEROEN"))
print(solution3("JAN"))
#print(solution("AAZ"))
print(solution3("ZZAAAZZ"))
print(solution3("ZZZAAAAAAAAZZZZ"))
#print(solution("AZAEAWAZAZ"))
#print(solution("BBBAAAB"))#9
#print(solution("ABABAAAAABA")) #11




