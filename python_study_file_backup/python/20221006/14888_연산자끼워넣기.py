
N = int(input())

num_list = list(map(int, input().split()))
#print(num_list)

# + - x //   :  operator
op_count = list(map(int, input().split()))
#print(op_count)

# 주어진 조건 중 수의 범위가 10억 이내일 경우 사용 가능
min_re = 1e9
max_re = -1e9


def cal_num(op, re, index):
    
    global min_re
    global max_re
    
    #if op.count(0) == 4:
    if index == N:
        #print('re? ',re)
        max_re = max(max_re, re)
        min_re = min(min_re, re)
        return
    
    for i in range(4):
        #print('??i??',i)
        if op[i] != 0:
            #print('1 op', op)
            op[i] -= 1
            #print('2 op', op)
            #print('?? re', re)
            if i == 0:
                cal_num(op, re + num_list[index], index+1)
            elif i == 1:
                cal_num(op, re - num_list[index], index+1)
            elif i == 2:
                cal_num(op, re * num_list[index], index+1)
            elif i == 3:
                if re < 0:
                    re *= -1
                    cal_num(op, (re // num_list[index])*(-1), index+1)
                else:
                    cal_num(op, re // num_list[index], index+1)
            op[i] += 1
            #print('!! re', re)
              
cal_num(op_count, num_list[0], 1)
print(max_re)
print(min_re)




