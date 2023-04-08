
'''
https://www.youtube.com/playlist?list=PL3xNAKVIm80KqKdgPzkZgmwt9U_eTQ2sM

https://www.youtube.com/watch?v=SZzYrBv0aRU

회전의 2가지 단계
1. transpose : 전치행렬로 만들고
2. reverse : 각 행마다 원소의 순서를 뒤집어줌

1. Transpose 전치행렬
왼쪽위 -> 오른쪽 아래까지의 대각선을 중심으로
대칭되는 원소들의 위치를 서로 뒤바꾼것

2중반복문사용
i: 행, j: 열
j < i 일 때 j++
swap하기 m[j][i] <-> m[i][j]


2. Reverse 직관적!

'''
N=4 
room = [[0 for _ in range(N)] for _ in range(N)]
num = 1
for i in range(N):
    for j in range(N):
        room[i][j] = num
        num += 1

print(room)

# transpose : 시계
for i in range(N):
    for j in range(N):
        if j < i:
            room[j][i], room[i][j] = room[i][j], room[j][i]
        else:
            break
print(room)

'''
# transpose : 반시계
for i in range(N):
    for j in range(N):
        if j+i < N-1:
            room[j][i], room[N-1-i][N-1-j] = room[N-1-i][N-1-j], room[j][i]
        else:
            break
print(room)
'''

# reverse
for i, r in enumerate(room):
    room[i] = r[-1::-1]

print(room)




