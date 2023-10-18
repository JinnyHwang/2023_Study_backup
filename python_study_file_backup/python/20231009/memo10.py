
# 필요한 정보는?
# 알파벳이 어떤 숫자로 대체되었는가
# 대체된 알파벳과 사칙연산 기호 계산
input_str = tuple(input())

alph_dic = {}
op_list = []
num_list = []
for ss in input_str:
    if ss in ('+','-','*'):
        op_list.append(ss)
    else:
        num_list.append(ss)
        alph_dic[ss] = alph_dic.get(ss,-1)
#print(alph_dic)
#print(op_list)
#print(num_list)
alph_dic_keys = list(alph_dic.keys())
#print(alph_dic_keys)
 
max_value = -2147483648 # 2**31


def cal_seg(oper, num1, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1*num2
    else:
        print('error')
        return 1e9
    
    
def cal_all():
    res = alph_dic[num_list[0]]
    idx = 1
    
    for i in range(len(op_list)):
        #print('i? ',i,' op_list[i], res, alph_dic[num_list[i+1]]', op_list[i], res, alph_dic[num_list[i+1]])
        res = cal_seg(op_list[i], res, alph_dic[num_list[i+1]])
    return res
    

# alph_dic의 모든 key값을 1~4 숫자로 채우는 재귀
def fill_alph_dic(cnt):
    global max_value
    
    if cnt == len(alph_dic_keys):
        #print(cal_all(), alph_dic)
        max_value = max(max_value, cal_all())
        return
    
    for ii in range(1,5):
        alph_dic[alph_dic_keys[cnt]] = ii
        fill_alph_dic(cnt+1)
    
    
fill_alph_dic(0)
print(max_value)






