def solution(clothes):
    
    clo_dic = {}
    
    for c in clothes:
        clo_dic[c[1]] = clo_dic.get(c[1], []) + [c[0]]
        
    cnt = [ 0 for i in range(len(clo_dic))]
    i = 0
    print(cnt)
    
    for k in clo_dic:
        # 현재 원소 개수
        cnt[i] = len(clo_dic[k])
        print(cnt[i])
        if i > 0:
            print('cnt[i] : ', cnt[i], 'cnt[i-1] : ', cnt[i-1], cnt[i-1]*(1 + cnt[i]))
            # 현재원소개수*이전원소개수 + 이전값
            cnt[i] += cnt[i-1]*(1 + cnt[i])
        print('cnt[i] : ', cnt[i])
        i += 1
    
    return cnt[-1]


l1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(l1)

l2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
#solution(l2)








