
'''
3
3 4 5
2 2

필요한 감독관 수의 최솟값?
'''

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
#print(N, A, B, C)

answer = 0

for i, a in enumerate(A):
    A[i] -= B
    answer += 1

#print(A, answer)

for a in A:
    if a > 0:
        answer += a//C
        if a%C > 0:
            answer += 1

print(answer)
        




