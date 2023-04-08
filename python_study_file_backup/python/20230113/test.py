
bi = [0,0,0,0,0,0]


print(bi)



def solution(n, lost, reserve):

    stu = [ 1 for _ in range(n)]
    print(stu)

    for l in lost:
        stu[l-1] -= 1
    print(stu)

    for r in reserve:
        stu[r-1] += 1
    print(stu)

    fail = 0
    for si, s in enumerate(stu):
        if si == n-1:
            break
        if s == 0:
            if si != 0 and stu[si-1] == 2:
                s, stu[si-1] = 1, 1
            elif stu[si+1] == 2:
                s, stu[si+1] = 1, 1
            else:
                fail += 1
    print(stu)
    answer = n - fail
    return answer


solution(5, [2,4], [1,3,5])

