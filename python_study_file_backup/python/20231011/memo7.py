
# 마을의 개수
# 같은 마을에 있는 사람의 수
city_people = []

n = int(input())
city_map = [ list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]

# 상 하 좌 우
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x,y):
    
    if not in_range(x,y):
        return False
    #print('??',x,y)
    if not city_map[x][y] or visited[x][y]:
        return False
    
    return True

people_num = 0
def dfs(x,y):
    global people_num
    
    visited[x][y] = 1
    #print(x,y)
    
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        
        if can_go(nx,ny):
            people_num += 1
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if city_map[i][j] and not visited[i][j]:
            #print('!start!')
            people_num = 1
            dfs(i,j)
            city_people.append(people_num)
            #print('people_num!',people_num)

city_people.sort()
print(len(city_people))
for c in city_people:
    print(c)



