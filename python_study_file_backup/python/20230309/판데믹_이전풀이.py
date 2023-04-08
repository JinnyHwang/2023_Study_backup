from collections import deque

def solution(rows, columns, max_virus, queries):

    v_map = [ [ 0 for _ in range(columns) ] for _ in range(rows) ]
    #print(v_map)

    vd = [(-1,0),(1,0),(0,-1),(0,1)]
    vq = deque()
    v_map_visited = [ [ 0 for _ in range(columns) ] for _ in range(rows) ]

    for qr,qc in queries:
        r = qr-1
        c = qc-1
        if v_map[r][c] < max_virus:
            v_map[r][c] += 1

        elif v_map[r][c] == max_virus:
            v_map_visited = [ [ 0 for _ in range(columns) ] for _ in range(rows) ]
            # 인접칸 확인
            vq.append([r,c])

            while vq:
                qr, qc = vq.pop()
                v_map_visited[qr][qc] = 1
                #print('qr: {}, qc: {}'.format(qr, qc ))
                for dr, dc in vd :
                    nr = qr+dr
                    nc = qc+dc
                    if 0 <= nr < rows and 0 <= nc < columns and v_map_visited[nr][nc]==0:
                        if v_map[nr][nc] == max_virus:
                            vq.append([nr, nc])
                        else:
                            v_map[nr][nc] += 1
                            v_map_visited[nr][nc] = 1                         
        #print(v_map)
    #print(v_map)       

    return v_map