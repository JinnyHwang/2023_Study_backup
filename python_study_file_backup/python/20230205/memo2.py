
# s1은 s2의 선수과목
def solution(s1, s2, k):
    
    print(s1, s2, k)
    
    # s_dic: key 과목을 들으려면 value 과목을 들어야함
    s_dic = {}
    for si, sv in enumerate(s2):
        s_dic[sv] = s_dic.get(sv, []) + [s1[si]]
    
    # 선수 과목이 여러개인 경우 알파벳 순서로.
    for dk in s_dic:
        s_dic[dk].sort(reverse=True)
    print(s_dic)
    
    '''
    if 'G' in s_dic:
        print('?1')
        
    if 'A' in s_dic:
        print('?2')
    else:
        print('?3')
    
    print(s_dic['G'].pop())
    print(s_dic['G'].pop())
    print(s_dic['G'])
    
    if not s_dic['G']:
        print('!1')
    else:
        print('!2')
    '''
    
    
    # k를 듣기 위한 선수 과목은?
    # s_dic[k]
    
    # 어떤 규칙으로 stack을 쌓아야할까?
    # 각 루트의 맨 끝들을 비교, 확인
    # 가능한 모든 그래프 만들고 하나로 합치기
    graphs = []
    s = []
    s.append(k)
    graphs.append(s)
    print(graphs)
    
    '''
    last_s = graphs[-1]
    key = last_s[-1]
  
    if key in s_dic and s_dic[key]:
        tmp_s = graphs.pop()
        
        while s_dic[key]:
            value = s_dic[key].pop()
            graphs.append(tmp_s+[value])
    print(graphs)
    '''
    
    while True:
        cnt = 0
        for g_i, g_s in enumerate(graphs):
            key = g_s[-1]
            
            if key in s_dic and s_dic[key]:
                tmp_s = g_s
                del graphs[g_i]
                
                while s_dic[key]:
                    value = s_dic[key].pop()
                    graphs.append(tmp_s+[value])
            else:
                cnt += 1
                
        if cnt == len(graphs):
            break
    
    # 모든 그래프
    print(graphs)
    
    answer = []
    
    for h in 
    
    
    
    return answer


s1_1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2_1 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k_1 = "B"

s1_2 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2_2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k_2 = "G"

#solution(s1_1, s2_1, k_1)
solution(s1_2, s2_2, k_2)

