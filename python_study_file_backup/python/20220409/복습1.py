
# 해쉬 딕셔너리
def solution1(participant, completion):
    
    dic = {}
    
    for p in participant:
        dic[p] = dic.get(p, 0)+1
    
    for c in completion:
        dic[c] = dic.get(c)-1
    
    for d in dic:
        if dic[d] > 0:
            return d
    
    

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
#print(solution1(participant1, completion1))

p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
c2 = ["josipa", "filipa", "marina", "nikola"]
#print(solution1(p2, c2))

p3 = ["mislav", "stanko", "mislav", "ana"]
c3 = ["stanko", "ana", "mislav"]
#print(solution1(p3, c3))




def solution2_test(phone_book):
    
    phone_book.sort()
    l = len(phone_book)
    
    for i1, p1 in enumerate(phone_book):
        if int(i1) == l-1:
            print('end?')
            break
        print('1: ', p1, i1, l-1, int(i1))
        for i2 in range(int(i1)+1, l):
            print('2: ', p1, phone_book[i2][:len(p1)])
            if p1 == phone_book[i2][:len(p1)]:
                return False
    return True

def solution2(phone_book):
    
    phone_book.sort()
    l = len(phone_book)
    
    for i1, p1 in enumerate(phone_book):
        if int(i1) == l-1:
            break
        for i2 in range(int(i1)+1, l):
            if p1 == phone_book[i2][:len(p1)]:
                return False
    return True

def solution2_ans(phone_book):
    phone_book.sort()
    # p = sorted(phone_book)
    l = len(phone_book)
    
    # sort했기 때문에 바로 다음 원소만 확인해도 ok
    # 모든 원소 탐색 필요 없음
    for i, p in enumerate(phone_book, start=1):
        # 마지막 원소도 확인해야 하므로 i<l
        if i<l and p in phone_book[i][:len(p)]:
            return False
            
    return True



pb1 = ["119", "97674223", "1195524421"]
pb2 = ["123","456","789"]
pb3 = ["12","123","1235","567","88"]

#pb1.sort()
#pb2.sort()
#pb3.sort(reverse=True)
#pb3.sort()
#print(pb1, pb2, pb3)

print(solution2_ans(pb1))
print(solution2_ans(pb2))
print(solution2_ans(pb3))



