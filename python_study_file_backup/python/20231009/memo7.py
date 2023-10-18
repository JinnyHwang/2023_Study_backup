
mapper = {'+':0, '-':1, '*':2}
#alph_dic = {}
#alph_dic[i] = alph_dic.get(i,0) + num

input_str = tuple(input())
max_value = 0
#for i,s in enumerate(input_str):
#    print(i, s)
memory_dic = {}

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
    

# 알파벳에 1~4 중 아무 숫자를 넣구 재귀 진행
def cal_all(cnt, alph_dic, value, key):
    global max_value, memory_dic
    
    if cnt == len(input_str):
        #print(memory_dic)
        max_value = max(max_value, value)
        return
    elif cnt == 0:
        alph = input_str[0]
        for i in range(1,5):
            #print('\ncnt0 alph? alph_dic?', alph, alph_dic)
            alph_dic[alph] = alph_dic.get(alph,i)
            nxt_value = value+alph_dic[alph]
            key += str(alph_dic[alph])
            memory_dic[key] = nxt_value
            cal_all(cnt+1, alph_dic, nxt_value, key)
            key = key[:-1]
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
            key = key + op + str(alph_dic[alph])
            
            if memory_dic.get(key):
                cal_all(cnt+2, alph_dic, memory_dic[key], key)
                key = key[:-2]
            else:
                nxt_value = cal_seg(mapper[op], value, alph_dic[alph])
                memory_dic[key] = nxt_value
                cal_all(cnt+2, alph_dic, nxt_value, key)
                key = key[:-2]
                alph_dic.pop(alph,None)
            
dic = {}
cal_all(0,dic,0,'')   
print(max_value)
    



