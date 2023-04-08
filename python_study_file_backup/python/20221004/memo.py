
arr = [3,6,8,11,24]

for i in range(len(arr)):
    #ans = [ a for a in arr ]
    ans2 = arr.copy()
    #print(ans)
    print(ans2)
    print(arr[i], ', ', ans2[i])
    del(ans2[i])
    print(ans2)
