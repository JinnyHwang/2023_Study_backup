
N, M = 5, 5
visited = [[ 0 for _ in range(M) ] for _ in range(N)]
print( 0 in visited[0] )
ll = [ True if 0 in v else for v in visited ]
print(ll)
#print( if 0 in v for v in visited )

'''
game_info = [ [[]]*N for _ in range(N) ]
이렇게 만들 경우 내부적으로 포함된 N개 리스트가
모두 동일 객체에 대한 N개의 레퍼런스로 인식함!
game_info[n][0], game_info[n][1], game_info[n][2], game_info[n][3] 모두 똑같은 객체
game_info
 [[[], [], [], []], [[0, 2], [0, 2], [0, 2], [0, 2]], [[1], [1], [1], [1]], [[3], [3], [3], [3]]]

# 컴프리헨션 사용!
game_info = [ [[] for _ in range(N)] for _ in range(N) ]
'''

info = [ [ [] for _ in range(3) ] for _ in range(5) ]
print(info)

N, M = map(int, input().split())

# 처음 초기화할 때 주소값을 할당하기 때문에 주소값 달라짐
visited1 = [[ m for m in range(M) ] for _ in range(N)]

# 맨 처음엔 data 할당하지 않아서 주소값 동일
# 값 할당하면 주소값 달라짐
visited = [[ 0 for _ in range(M) ] for _ in range(N)]
print(visited)

print(id(visited[0][0]))
print(id(visited[0][1]))
# 1799809520
# 1799809520

print(id(visited[0]))
print(id(visited[1]))
# 65590656
# 65591376

print(visited[0][0] == visited[0][1])
print(id(visited[0][0]) == id(visited[0][1]))
# True
# True

visited[0][0] = 3
print(id(visited[0][0]))
print(id(visited[0][1]))
# 1799809568
# 1799809520










