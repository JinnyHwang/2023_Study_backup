
import time

n = int(input("Number of elements: "))
haystack = [k for k in range(n)]

print("Searching for the maximun value")

ts = time.time()
maximum = max(haystack) #개수에 비례하는 만큼 시간이 걸린다
elapsed = time.time()-ts

print("Maxinum element = %d, Elapsed time = %.2f"%(maximum, elapsed))


# 다른 자료구조를 사용하면 걸리는 시간을 단축시킬 수 있다
# 각 상황에 맞는 자료구조를 사용해야한다. 최적의 해법을 찾는 것.
# 연산: 최대값, 특정원소 찾기, 삽입, 삭제 등
# 알고리즘: 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택
