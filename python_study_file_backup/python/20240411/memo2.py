

def roll_dice(cmd, dice_up, dice_front, dice_right):
    
    if cmd == 'L':
        #up = right
        #front = front
        #right = 7-up 
        return (dice_right, dice_front, 7-dice_up)
        
    elif cmd == 'R':
        #up = 7-right
        #front = front
        #right = up
        return (7-dice_right, dice_front, dice_up)
    
    elif cmd == 'U':
        #up = front
        #front = 7-up
        #right = right
        return (dice_front, 7-dice_up, dice_right)
        
    elif cmd == 'D':
        #up = 7-front
        #front = up
        #right = right
        return (7-dice_front, dice_up, dice_right)


cmd_map = {'L':0, 'R':1, 'U':2, 'D':3 }
n, m, r, c = map(int, input().split())
input_cmd = list(input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
x, y = r-1, c-1

dice_up = 1
dice_front = 2
dice_right = 3

#  ‘L', ‘R’, ‘U’, 'D’
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()

grid[x][y] = 7-dice_up
for cmd in input_cmd:
    #print(cmd, x, y, dice_up, dice_front, dice_right)
    dice_d = cmd_map[cmd]
    nx, ny = x+dxs[dice_d], y+dys[dice_d]
    if in_range(nx, ny):
        dice_up, dice_front, dice_right = roll_dice(cmd, dice_up, dice_front, dice_right)
        x, y = nx, ny
    grid[x][y] = 7-dice_up
  
#print_grid(grid)

result = 0
for g in grid:
    for gg in g:
        result += gg

print(result)



