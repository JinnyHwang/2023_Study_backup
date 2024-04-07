
input_str = input()

def Encode(str1):
    new_str = ''
    now_chr = str1[0]
    cnt = 1
    for i in range(1, len(str1)):
        if now_chr == str1[i]:
            cnt += 1
        else:
            new_str += now_chr
            new_str += str(cnt)
            now_chr = str1[i]
            cnt = 1
    new_str += now_chr
    new_str += str(cnt)
    
    return new_str
            
#print(Encode(input_str))
#print(len(Encode(input_str)))

# shift횟수는?
#print(input_str[::-1])
#print(input_str[-1]+input_str[:len(input_str)-1])
#chk_str = input_str[-1]+input_str[:len(input_str)-1]
chk_str = input_str[-1]+input_str[:-1]
#min_len = 1000
min_len = len(Encode(input_str)) # shift안했을 때 초기값!
for _ in range(len(input_str)-1):
    #print(chk_str)
    #print(Encode(chk_str), len(Encode(chk_str)))
    min_len = min(min_len, len(Encode(chk_str)))
    #chk_str = chk_str[-1]+chk_str[:len(chk_str)-1]
    chk_str = chk_str[-1]+chk_str[:-1]
    
print(min_len)
