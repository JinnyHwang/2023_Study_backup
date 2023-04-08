import time

# 0 ~ n-1 까지의 나열된 리스트 생성
n = int(input("개수 : "))
haystack = [k for k in range(n)]

print("Searching for the maximum value!")

# 현재 시간을 불러오는 time() api
ts = time.time()
maximum = max(haystack)
elapsed = time.time() - ts

print("Maximun element = %d , Elapsed time = %.2f" % (maximum, elapsed))
# 해당 방법은 모든 리스트를 탐색
# max()를 사용하면 탐색하는 시간이 원소 개수에 비례함

# 가장 빨리 원소를 찾을 수 있는 방법은?
# 각 상황에 맞는 자료구조가 다양하게 있음

# 알고리즘
# 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택

