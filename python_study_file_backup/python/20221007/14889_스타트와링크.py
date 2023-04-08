#https://www.acmicpc.net/problem/14889

N = int(input())

ability_map = [ list(map(int, input().split())) for _ in range(N) ]

'''
12 34
34 12
값은 동일하다

탐색은
N/2까지만 해도..?

'''

def cal_ability(l):
    l_sum = 0
    
    for i in l:
        for j in l:
            if i != j:
                l_sum += ability_map[i][j]
    
    return l_sum        
    

min_data = 1e9

def team(index, list_1):
    global min_data
    
    if len(list_1) == N//2:
        
        list_2 = []
        for i in range(N):
            if i not in list_1:
                list_2.append(i)
        
        #print('list_1: ', list_1)
        #print('list_2: ', list_2)
        
        #print('cal_ability(list_1)? ', cal_ability(list_1))
        #print('cal_ability(list_2)? ', cal_ability(list_2))
        
        min_data = min(min_data, abs(cal_ability(list_1) - cal_ability(list_2)))
        
        #print('min_data? ', min_data)
        
        return
    

    for i in range(index, N):
        
        if len(list_1) == 0 and i == (N//2)-1:
            break
        
        list_1.append(i)
        #print('???',list_1)
        team(i+1, list_1)
        
        list_1.remove(i)
        #print('!!!',list_1)
        
            
            
l1 = []
team(0, l1)
print(min_data)





