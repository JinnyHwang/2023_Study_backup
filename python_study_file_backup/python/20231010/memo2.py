
n, m = tuple(map(int, input().split()))
num_list = list(map(int, input().split()))
num_combi = []
max_re = 0

def cal_XOR():
    re = 0
    for ll in num_combi:
        re = re^ll
    #print(re)
    return re

# num_list 숫자중 m개를 뽑아서 xor 결과 최대값 출력
# xor 결과는 순서와 상관 없으므로 조합으로!
def combinate(cnt,idx):
    global max_re
    
    if cnt == m:
        #print(num_combi)
        max_re = max(max_re, cal_XOR())
        return
    
    for i, n in enumerate(num_list):
        if i > idx:
            num_combi.append(n)
            combinate(cnt+1,i)
            num_combi.pop()
    '''
    for i in num_list:
        if i not in num_combi:
            num_combi.append(i)
            combinate(cnt+1)
            num_combi.pop()
    '''

combinate(0,-1)
print(max_re)
