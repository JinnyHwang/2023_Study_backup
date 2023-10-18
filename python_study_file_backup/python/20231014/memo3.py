grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

a = 4
b = 2
new_grid = [[0 for _ in range(4)] for _ in range(4)]
for i in range(a):
    for j in range(b):
        rx, ry = j+(a-b), a-i-1
        print(i,j,grid[i][j])
        print(rx,ry,grid[rx][ry])
        new_grid[rx][ry] = grid[i][j]
print(grid)
print(new_grid)



