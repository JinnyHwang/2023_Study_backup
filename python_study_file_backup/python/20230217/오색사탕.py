

def solution(candy, positions):

    # part1
    n_match, cache = 0, [0]*len(candy)
    print(candy)
    for i in range(1, len(candy)):
        print(i, '번째 탐색 : ', cache)
        while n_match and candy[n_match] != candy[i]:
            print('n_match:{} i:{} / cache[n_match]:{}'.format(n_match, i, cache[n_match]))
            n_match = cache[n_match]
            
        if candy[n_match] == candy[i]:
            print('n_match:{} {}  i:{} {}  '.format(n_match, candy[n_match], i, candy[i]))
            n_match += 1
            cache[i] = n_match
            print('n_match?{} cache[i]?{}'.format(n_match, cache[i]))
    
    # part2
    answer = []
    print('cache: ',cache)
    for pos in positions:
        print(pos, ' 확인시작!')
        ans = 0
        while cache[pos-1]:
            print('pos? {}\tcache[pos-1]? {}'.format(pos,cache[pos-1]))
            pos = cache[pos-1]
            ans += 1
        answer.append(ans)
        
    return answer



candy1 = "RYRYRGPRYRYRBB"
candy2 = "RYRYRRPRYRYRBB"
positions1 = [12, 1, 14, 7]

solution(candy1, positions1)






