
# https://yangnyang.tistory.com/14

# 순열
# N개 중 r개 선택해서 만들 수 있는 모든 경우의 수(순서상관있음)
# Permutations(list, num)

# 직접 구현해보기
def perm(arr, n):
    result = []
    
    if n > len(arr):
        print('end result? ', result)
        return result
    
    # n이 1일 때 arr안 모든 원소를 result에 넣는다
    if n == 1:
        print('??arr?? ', arr)
        for i in arr:
            result.append([i])
            print('result? ', result)
    elif n > 1:
        for i in range(len(arr)):
            ans = arr.copy()
            print('ans? ', ans, '   ans[i]? ', ans[i])
            # index 앞쪽 부터 delete
            del(ans[i])
            
            # 이 구문을 이해하기!
            for p in perm(ans, n-1):
                # perm(ans, n-1)의 return 값을 하나씩 arr[i]에 붙이기
                print('arr? ', arr, '   arr[i]? ', arr[i], '  p? ', p)
                result.append([arr[i]]+p)
    return result
        
arr = [3,6,8,11]
#print(perm(arr,3))

'''
ans?  [3, 6, 8, 11]    ans[i]?  3
ans?  [6, 8, 11]    ans[i]?  6
??arr??  [8, 11]
result?  [[8]]
result?  [[8], [11]]
arr?  [6, 8, 11]    arr[i]?  6   p?  [8]
arr?  [6, 8, 11]    arr[i]?  6   p?  [11]
ans?  [6, 8, 11]    ans[i]?  8
??arr??  [6, 11]
result?  [[6]]
result?  [[6], [11]]
arr?  [6, 8, 11]    arr[i]?  8   p?  [6]
arr?  [6, 8, 11]    arr[i]?  8   p?  [11]
ans?  [6, 8, 11]    ans[i]?  11
??arr??  [6, 8]
result?  [[6]]
result?  [[6], [8]]
arr?  [6, 8, 11]    arr[i]?  11   p?  [6]
arr?  [6, 8, 11]    arr[i]?  11   p?  [8]
arr?  [3, 6, 8, 11]    arr[i]?  3   p?  [6, 8]
arr?  [3, 6, 8, 11]    arr[i]?  3   p?  [6, 11]
arr?  [3, 6, 8, 11]    arr[i]?  3   p?  [8, 6]
arr?  [3, 6, 8, 11]    arr[i]?  3   p?  [8, 11]
arr?  [3, 6, 8, 11]    arr[i]?  3   p?  [11, 6]
arr?  [3, 6, 8, 11]    arr[i]?  3   p?  [11, 8]
ans?  [3, 6, 8, 11]    ans[i]?  6
ans?  [3, 8, 11]    ans[i]?  3
??arr??  [8, 11]
result?  [[8]]
result?  [[8], [11]]
arr?  [3, 8, 11]    arr[i]?  3   p?  [8]
arr?  [3, 8, 11]    arr[i]?  3   p?  [11]
ans?  [3, 8, 11]    ans[i]?  8
??arr??  [3, 11]
result?  [[3]]
result?  [[3], [11]]
arr?  [3, 8, 11]    arr[i]?  8   p?  [3]
arr?  [3, 8, 11]    arr[i]?  8   p?  [11]
ans?  [3, 8, 11]    ans[i]?  11
??arr??  [3, 8]
result?  [[3]]
result?  [[3], [8]]
arr?  [3, 8, 11]    arr[i]?  11   p?  [3]
arr?  [3, 8, 11]    arr[i]?  11   p?  [8]
arr?  [3, 6, 8, 11]    arr[i]?  6   p?  [3, 8]
arr?  [3, 6, 8, 11]    arr[i]?  6   p?  [3, 11]
arr?  [3, 6, 8, 11]    arr[i]?  6   p?  [8, 3]
arr?  [3, 6, 8, 11]    arr[i]?  6   p?  [8, 11]
arr?  [3, 6, 8, 11]    arr[i]?  6   p?  [11, 3]
arr?  [3, 6, 8, 11]    arr[i]?  6   p?  [11, 8]
ans?  [3, 6, 8, 11]    ans[i]?  8
ans?  [3, 6, 11]    ans[i]?  3
??arr??  [6, 11]
result?  [[6]]
result?  [[6], [11]]
arr?  [3, 6, 11]    arr[i]?  3   p?  [6]
arr?  [3, 6, 11]    arr[i]?  3   p?  [11]
ans?  [3, 6, 11]    ans[i]?  6
??arr??  [3, 11]
result?  [[3]]
result?  [[3], [11]]
arr?  [3, 6, 11]    arr[i]?  6   p?  [3]
arr?  [3, 6, 11]    arr[i]?  6   p?  [11]
ans?  [3, 6, 11]    ans[i]?  11
??arr??  [3, 6]
result?  [[3]]
result?  [[3], [6]]
arr?  [3, 6, 11]    arr[i]?  11   p?  [3]
arr?  [3, 6, 11]    arr[i]?  11   p?  [6]
arr?  [3, 6, 8, 11]    arr[i]?  8   p?  [3, 6]
arr?  [3, 6, 8, 11]    arr[i]?  8   p?  [3, 11]
arr?  [3, 6, 8, 11]    arr[i]?  8   p?  [6, 3]
arr?  [3, 6, 8, 11]    arr[i]?  8   p?  [6, 11]
arr?  [3, 6, 8, 11]    arr[i]?  8   p?  [11, 3]
arr?  [3, 6, 8, 11]    arr[i]?  8   p?  [11, 6]
ans?  [3, 6, 8, 11]    ans[i]?  11
ans?  [3, 6, 8]    ans[i]?  3
??arr??  [6, 8]
result?  [[6]]
result?  [[6], [8]]
arr?  [3, 6, 8]    arr[i]?  3   p?  [6]
arr?  [3, 6, 8]    arr[i]?  3   p?  [8]
ans?  [3, 6, 8]    ans[i]?  6
??arr??  [3, 8]
result?  [[3]]
result?  [[3], [8]]
arr?  [3, 6, 8]    arr[i]?  6   p?  [3]
arr?  [3, 6, 8]    arr[i]?  6   p?  [8]
ans?  [3, 6, 8]    ans[i]?  8
??arr??  [3, 6]
result?  [[3]]
result?  [[3], [6]]
arr?  [3, 6, 8]    arr[i]?  8   p?  [3]
arr?  [3, 6, 8]    arr[i]?  8   p?  [6]
arr?  [3, 6, 8, 11]    arr[i]?  11   p?  [3, 6]
arr?  [3, 6, 8, 11]    arr[i]?  11   p?  [3, 8]
arr?  [3, 6, 8, 11]    arr[i]?  11   p?  [6, 3]
arr?  [3, 6, 8, 11]    arr[i]?  11   p?  [6, 8]
arr?  [3, 6, 8, 11]    arr[i]?  11   p?  [8, 3]
arr?  [3, 6, 8, 11]    arr[i]?  11   p?  [8, 6]
[[3, 6, 8], [3, 6, 11], [3, 8, 6], [3, 8, 11], [3, 11, 6], [3, 11, 8], [6, 3, 8], [6, 3, 11], [6, 8, 3], [6, 8, 11], [6, 11, 3], [6, 11, 8], [8, 3, 6], [8, 3, 11], [8, 6, 3], [8, 6, 11], [8, 11, 3], [8, 11, 6], [11, 3, 6], [11, 3, 8], [11, 6, 3], [11, 6, 8], [11, 8, 3], [11, 8, 6]]
'''



# 조합
# N개 중 순서 상관 없이 r개로 만들 수 있는 모든 경우의 수
# Combinations(list, num)

def comb(arr, n):
    result = []
    if n > len(arr):
        print('end result? ', result)
        return result
    
    if n == 1:
        print('arr? ', arr)
        for i in arr:
            result.append([i])
            print('?? result?? ', result)
    elif n > 1:
        print('len(arr) - n +1? ', len(arr) - n +1)
        for i in range(len(arr) - n +1):
            print(' i? ',i, '  n? ', n)
            for j in comb(arr[i+1:], n-1):
                print('arr[i]? ', arr[i], ' j? ', j)
                result.append([arr[i]]+j)
    return result


arr = [3,6,8,11,24, 33, 41]
print(comb(arr, 3))



