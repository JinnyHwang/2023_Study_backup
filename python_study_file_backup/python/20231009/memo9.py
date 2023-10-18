mapper = {'+':0, '-':1, '*':2}
#alph_dic = {}
#alph_dic[i] = alph_dic.get(i,0) + num

input_str = tuple(input())
max_value = -2147483648 # 2**31
#for i,s in enumerate(input_str):
#    print(i, s)

def cal_seg(oper, num1, num2):
    
    if oper == 0:
        return num1 + num2
    elif oper == 1:
        return num1 - num2
    elif oper == 2:
        return num1*num2
    else:
        print('error')
        return 1e9
    
def cal_a_op(alph_dic):
    cal_re = alph_dic[input_str[0]]
    idx = 1
    while idx < len(input_str):
        if input_str[idx] == '+':
            cal_re += alph_dic[input_str[idx+1]]
            idx += 2
        elif input_str[idx] == '-':
            cal_re -= alph_dic[input_str[idx+1]]
            idx += 2
        elif input_str[idx] == '*':
            cal_re *= alph_dic[input_str[idx+1]]
            idx += 2
        else:
            print('error')
            break
    return cal_re
        
    


# 알파벳에 1~4 중 아무 숫자를 넣구 재귀 진행
def cal_all(cnt, alph_dic):
    global max_value
    
    if cnt == len(input_str):
        max_value = max(max_value, cal_a_op(alph_dic))
        return
    elif cnt == 0:
        alph = input_str[0]
        for i in range(1,5):
            #print('\ncnt0 alph? alph_dic?', alph, alph_dic)
            alph_dic[alph] = alph_dic.get(alph,i)
            cal_all(cnt+1, alph_dic)
            alph_dic.pop(alph,None)
    else:
        # input_str[cnt] : 부호
        # input_str[cnt+1] : 알파벳
        op = input_str[cnt]
        alph = input_str[cnt+1]
        for i in range(1,5):
            if not alph_dic.get(alph):
                alph_dic[alph] = alph_dic.get(alph,i)
            #print('\ncnt: ', cnt,' alph? alph_dic?', alph, alph_dic)
            cal_all(cnt+2, alph_dic)
            alph_dic.pop(alph,None)


dic = {}
cal_all(0,dic)
print(max_value)
