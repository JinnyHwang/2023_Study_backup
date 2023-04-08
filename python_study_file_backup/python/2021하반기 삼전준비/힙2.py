import heapq
def solution1(jobs):
    
     # 끝나는 시간 = 시작시간 + 대기시간 + 작업시간
    # 현재 진행중인 job
    # 현재 시간에서 남아있는 job -> 가장 짧은거 정렬 -> min heap
    # 긴 job을 먼저하면 이후 기다리는 job의 대기시간이 커지기 때문
    # 만약 작업이 없음 -> 먼저들어오는것부터
    # 시작시간을 보고 jobs 리스트를 pop
    # pop한 원소의 작업시간을 보고 job heap 추가 (min heap 정렬)
    # jobs가 없고, job heap 비었을 때 end
    # time return
    
    
    
    # jobs 리스트 원소에 하나씩 탐색
    # ㄴ여기서 lambda x : x[1]의 의미는
    # sort하는 리스트의 각 원소의 1번인덱스 값을 의미
 #   jobs.sort(key=lambda x : x[1])    
 #   print((lambda x : x[1][0])([[0, 3], [7, -1], [2, 6]]))
    
    # 각 원소의 첫번째 값으로 sorting됨
  #  jobs.sort()
    
    # 해당 시간에 진행되는 job
    jobs_dic = {}
    
    for a in jobs:
        jobs_dic[a[0]] = jobs_dic.get(a[0], []) + [a[1]]
    
   # print(jobs_dic)
    
    # 현재 시간에 진행해야하는 작업리스트
    dojob = []
    
    time = 0
    all_time = 0
    curr_job_countdown = 0
    
    print(jobs_dic)
    while True:
        
        print("!!curr time: ", time)
    #     print(jobs_dic.get(time))
        if jobs_dic.get(time) :
            for j in jobs_dic.get(time):
                heapq.heappush(dojob, [j, time])
            #print(time, dojob)
            jobs_dic.pop(time)
            print("pop jobs_dic: ",jobs_dic)
            print("push dojob: ",dojob)
       # else:
       #     print(time, "dict key check pass")
        
        # 현재 진행중인 job 없음.
        if curr_job_countdown == 0 and len(dojob) > 0:
            curr_j = heapq.heappop(dojob)
            print("(time - curr_j[0]):{} curr_j[1]:{}".format((time - curr_j[0]), curr_j[1]))
            all_time += ((time - curr_j[1]) + curr_j[0])
            curr_job_countdown = curr_j[0]
            print("all_time: {}, curr_job_countdown: {}".format(all_time, curr_job_countdown))
            print("pop dojob: ",dojob)
        
        time += 1
        curr_job_countdown -= 1
        
        if len(jobs_dic) == 0 and len(dojob) == 0 and curr_job_countdown == 0:
            break
        
    #print(heapq.heappop(dojob), heapq.heappop(dojob),
    #      heapq.heappop(dojob), heapq.heappop(dojob), heapq.heappop(dojob))
    
    return all_time//len(jobs)



def solution2(jobs):
    
  #  jobs_dic = {}
    
  #  for a in jobs:
  #      jobs_dic[a[0]] = jobs_dic.get(a[0], []) + [a[1]]
    
    dojob = []
    
    time = 0
    all_time = 0
    curr_job_countdown = 0
    jobs_len = len(jobs)
    
    while True:
        
        print("!!curr time: ", time, "curr_job_countdown: ", curr_job_countdown)
        
        if len(jobs) > 0 and jobs[0][0] == time :
            while True:
                if len(jobs) == 0:
                    break
                if jobs[0][0] == time:
                    j = jobs.pop(0)
                    heapq.heappush(dojob, [j[1], j[0]])
                else:
                    break
            print("pop jobs: ",jobs, "\npush dojob: ",dojob)
        
        elif curr_job_countdown == 0 and len(dojob) == 0:
            time = jobs[0][0]
          #  all_time += jobs[0][0]
            print("change time: ", time)
            continue
        elif len(dojob) == 0 and curr_job_countdown < jobs[0][0]:
            time += curr_job_countdown
            curr_job_countdown = 0
            print("change time(curr_job_countdown): ", time, "\tjobs[0][0]:", jobs[0][0])
            continue
       
       # if jobs_dic.get(time) :
       #     for j in jobs_dic.get(time):
       #         heapq.heappush(dojob, [j, time])
       #     jobs_dic.pop(time)
        
        # 현재 진행중인 job 없음.
        if curr_job_countdown == 0 and len(dojob) > 0:
            curr_j = heapq.heappop(dojob)
            print("(time - curr_j[0]):{} curr_j[1]:{}".format((time - curr_j[0]), curr_j[1]))
            all_time += ((time - curr_j[1]) + curr_j[0])
            curr_job_countdown = curr_j[0]
            print("all_time: {}, curr_job_countdown: {}".format(all_time, curr_job_countdown))
            print("pop dojob: ",dojob)
        
      #  if len(jobs_dic) > 0 and curr_job_countdown == 0 and len(dojob) == 0:
      #      jobs_dic.get(time)
      
        if len(jobs) == 0 and len(dojob) == 0:
            break
        
        time += 1
        curr_job_countdown -= 1

    return all_time//jobs_len


def solution3(jobs):
     
    dojob = []
    
    time = 0
    all_time = 0
    curr_job_countdown = 0
    jobs_len = len(jobs)
    
    while True:
        
        if len(jobs) > 0 and jobs[0][0] == time :
            while jobs:
                if jobs[0][0] == time:
                    j = jobs.pop(0)
                    heapq.heappush(dojob, [j[1], j[0]])
                else:
                    break
        
        elif curr_job_countdown == 0 and len(dojob) == 0:
            time = jobs[0][0]
            continue
        elif len(dojob) == 0 and curr_job_countdown < (jobs[0][0]-time):
            time += curr_job_countdown
            curr_job_countdown = 0
            continue
       
        # 현재 진행중인 job 없음.
        if curr_job_countdown == 0 and len(dojob) > 0:
            curr_j = heapq.heappop(dojob)
            all_time += ((time - curr_j[1]) + curr_j[0])
            curr_job_countdown = curr_j[0]
            
        if len(jobs) == 0 and len(dojob) == 0:
            break
            
        time += 1
        curr_job_countdown -= 1
        
    return all_time//jobs_len

def solution_1(jobs):
     
    dojob = []
    
    time = 0
    all_time = 0
    curr_job_countdown = 0
    jobs_len = len(jobs)
    
    while True:
        
        if len(jobs) > 0:
            # 해당 time에 시작되는 job을 dojob 리스트에 넣기
            if jobs[0][0] == time :
                while jobs :
                    if jobs[0][0] == time:
                        j = jobs.pop(0)
                        heapq.heappush(dojob, [j[1], j[0]])
                    else:
                        break
            # 앞으로 해야할 job 이 없을 때, time change
            elif len(dojob) == 0 :
                #지금 진행중인 job이 끝나는 시간과 다음 job까지의 시간이 좀 남음
                if curr_job_countdown < (jobs[0][0]-time):
                    time += curr_job_countdown
                    curr_job_countdown = 0
                    continue
                #지금 진행중인 job도 없음
                elif curr_job_countdown == 0 : 
                    time = jobs[0][0]
                    continue
        elif len(jobs) == 0 and len(dojob) == 0:
            break
                    
        if curr_job_countdown == 0 and len(dojob) > 0:
            curr_j = heapq.heappop(dojob)
            all_time += ((time - curr_j[1]) + curr_j[0])
            curr_job_countdown = curr_j[0]
            
        time += 1
        curr_job_countdown -= 1
        
    return all_time//jobs_len

def solution(jobs):
     
    dojob = []
    
    time = 0
    all_time = 0
    curr_job_countdown = 0
    jobs_len = len(jobs)
    
    while True:
        
        # 해당 time에 시작되는 job을 dojob 리스트에 넣기
        if len(jobs) > 0 and jobs[0][0] == time :
            while jobs :
                if jobs[0][0] == time:
                    j = jobs.pop(0)
                    heapq.heappush(dojob, [j[1], j[0]])
                else:
                    break
        # 현재 진행중인 job이 없고, 해야할 job도 없을 때
        elif curr_job_countdown == 0 and len(dojob) == 0:
            time = jobs[0][0]
            continue
        # 
        elif len(dojob) == 0 and curr_job_countdown < (jobs[0][0]-time):
            time += curr_job_countdown
            curr_job_countdown = 0
            continue
                
        if curr_job_countdown == 0 and len(dojob) > 0:
            curr_j = heapq.heappop(dojob)
            all_time += ((time - curr_j[1]) + curr_j[0])
            curr_job_countdown = curr_j[0]
                
        time += 1
        curr_job_countdown -= 1
        
        if len(jobs) == 0 and len(dojob) == 0:
            break
        
    return all_time//jobs_len

l1 = [[0, 3], [1, 9], [2, 6]]
l2 = [[0, 3], [1, 9], [2, 6], [0, 4], [0, 2], [4, 2]]
l3 = [[0, 3], [1, 9], [2, 6], [100, 4], [101, 2], [55, 2]]
l4 = [[0, 10], [4, 10], [15, 2], [5, 11]]





print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[100, 100], [1000, 1000]]), 550)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))

#print(solution2(l1))

#solution([[0, 3], [1, 9], [2, 6]])
#solution([[0, 3], [1, 9], [2, 6], [0, 4], [0, 2], [4, 2]])
#solution([[0, 3], [7, -1], [2, 6]])