
# 2n개 숫자 주어짐
# n개씩 2개 그룹으로 나눔
# 원소 합의 차 최소
# 주어진 자연수로 조합 2개 만들기

# 1~2n/2개 까지 기준점으로 조합 만들기
n = int(input())
num_list = list(map(int, input().split()))
visited = [0 for _ in range(2*n)]
combi_list = []

all_sum = sum(num_list)
#print(all_sum)
min_data = 1e9
def make_combi(cnt, idx):
    global min_data
    
    if cnt == n:
        #print(combi_list)
        #print(visited)
        sum_com_l = sum(combi_list)
        #print(all_sum, sum_com_l, all_sum-sum_com_l, (all_sum-sum_com_l)-sum_com_l)
        min_data = min(min_data, abs((all_sum-sum_com_l)-sum_com_l))
        return
    
    for i in range(2*n):
        if not combi_list and i >= 1:
            return
        
        if i > idx:
            combi_list.append(num_list[i])
            visited[i] += 1
            make_combi(cnt+1, i)
            combi_list.pop()
            visited[i] -= 1
    
make_combi(0,-1)
print(min_data)
