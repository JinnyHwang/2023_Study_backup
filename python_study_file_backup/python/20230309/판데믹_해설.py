# 해설은 DFS로 내 풀이는 queue를 사용한 BFS로 진행
# max_virus 이하면 숫자 1 증가
# max_virus면 주변을 stack에 추가
def solution(row, colums, max_virus, querise):
    
    virus_map = [ [0 for _ in range(colums)] for _ in range(row) ]
    #vd = [(0,1),(0,-1),(1,0),(-1,0)]
    
    # 내가 작성했던 code는 매 턴마다 visited 초기화해줌
    # 중첩 함수 사용하면 초기화 code 별도로 필요하지 않음
    def action(r, c):
        # 탐색할 좌표 stack에 쌓음
        stack = [(r,c)]
        visited = set((r,c))
        while stack:
            sr, sc = stack.pop()
            if virus_map[sr][sc] < max_virus:
                virus_map[sr][sc] += 1
            else: # stack에 넣음
                for _i, _j in [(sr,sc-1), (sr,sc+1), (sr-1,sc), (sr+1,sc)]:
                    if 0 <= _i < row and 0<= _j < colums and (_i,_j) not in visited:
                        stack.append((_i,_j))
                        visited.add((_i,_j))
                    
    
    # 중첩 함수를 사용하여 DFS 진행
    for qr, qc in querise:
        action(qr-1, qc-1) # 배열은 0분터 시작하므로
    
    return virus_map


r1 = 3
c1 = 4
mv1 = 2
q1 = [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]
print(solution(r1, c1, mv1, q1))


