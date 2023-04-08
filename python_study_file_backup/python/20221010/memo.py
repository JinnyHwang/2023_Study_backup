

N = 2

pic_group = []
pic_group_pos = []

# 각 그룹 탐색하기
for y in range(N):
    for x in range(N):
        print('\n??')
        pic_group.append([y+x, 1])
        pic_group_pos.append([[y,x]])
        print('1: ',pic_group)
        print('2: ',pic_group_pos)
        print('3: ',pic_group[-1])
        print('4: ',pic_group_pos[-1])
        pic_group[-1][1] = -1
        pic_group_pos[-1].append([3,5])
        pic_group_pos[-1].append([-7,7])
        print('5: ',pic_group)
        print('6: ',pic_group_pos)
        print('7: ',len(pic_group), len(pic_group_pos))


# 회전 연습
# 시계

# 반시계




l1 = [[0,0],[1,3],[4,11],[1,70],[50,101]]
print([4,11] in l1)
print([-1,11] in l1)


def show(arr):
    for a in arr:
        print(a)
    print('\n')
    

wall_map = [ [ [0 for _ in range(4) ] for _ in range(8) ] for _ in range(7) ]
show(wall_map)


l1 = [4, 4, 1]
l1[0] -= 1
l1[1] -= 1
print(l1)

l2 = [4, 4, 1]
l3 = [-1,-1]
l2[:2] = [ i1+i2 for i1, i2 in zip(l2,l3)]
print(l2)

l1 = [4,4,1]
l2 = [-1,-1]
l3 = [i1+i2 for i1, i2 in zip(l1, l2)]
print(l3)


N = int(input())

l4 = [-1,-1]
l5 = []
l6 = []
for _ in range(N):
    l5 = list(map(int, input().split()))
    l5[:2] = [ i1+i2 for i1, i2 in zip(l4,l5)]
    l6.append(l5)

print(l6)


