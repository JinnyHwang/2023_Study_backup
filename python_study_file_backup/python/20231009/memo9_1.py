express=list(input())

ope_list=[]
num_list=[]
for ex in express:
    if ex in ('+','-','*'):
        ope_list.append(ex)
    else:
        num_list.append(ex)


def calc(n1,n2,ope):
    if ope=='+':
        return n1+n2
    elif ope=='-':
        return n1-n2
    elif ope=='*':
        return n1*n2


def calcTotal(l):
    ans = l[0]
    for i in range(1,len(l)):
        ans=calc(ans,l[i],ope_list[i-1])
    return ans

def operation(num_idx,n):
    global maxAns
    if n==len(num_list):
        # print(l)
        # print(num_dict)
        result=calcTotal(l)
        if result>maxAns:
            maxAns=result
        return
    num=num_list[num_idx]
    if num_dict.get(num):
        l.append(num_dict[num])
        operation(num_idx+1,n+1)
        l.pop()
        return
    for i in range(1,5):
        num_dict[num]=i
        l.append(i)
        operation(num_idx+1,n+1)
        l.pop()
        num_dict.pop(num)
    return

num_dict={}
l=[]
maxAns=-987654321
operation(0,0)
print(maxAns)

