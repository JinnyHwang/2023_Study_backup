
'''
업무 처리에 10분이 걸림

예약 고객 중 먼저 도착한 고객 업무 처리
예약 고객이 없으면 일반 고객 업무 처리
시작 업무는 중단하지 않음
일반고객 업무처리 중 예약고객이 도착하면
일반고객 업무 후 예약고객 처리

[도착시각, 이름]
booked
unbooked

도착시간 순으로 정렬되어 있음
도착시간이 같은 고객은 없음

hh:mm 은 00:01~23:50 범위
오늘 하루 동안 온 고객 정보만 주어짐

업무처리 순서로 정렬된 이름 배열 return
'''


def solution(booked, unbooked):
    
    booked = [ ["09:55","hae"], ["10:05","jee"] ]
    unbooked = [ ["10:04","hee"], ["14:07","eom"] ]
    
    '''
    booked 와 unbooked 리스트를 pop(0) 하면서 확인 -> queue나 역순으로 정렬해서 pop()을 할까?
    
    booked, unbooked의 방문 시간은 정렬을 위한 기준치
    
    업무 처리 순서를 확인한 고객 정보를 담을 때 실제 해당 고객의 업무 처리 시작 시간 저장
    
    업무를 처리한 고객 이름 리스트와 실제 업무 시작 시간 저장
    
    
    # 확인 후 pop(0)을 진행 0번째 원소를 리스트 내에서 가장 빨리 처리해야하는 고객
    1. booked[0] unbooked[0] 리스트 원소 비교
    -> 현재 업무 진행 중인가?
    ----> 업무 진행중 시간에 booked[0] 사람이 도착했으면, 도착시간 무시하고 booked 사람 push
    ----> 업무 진행중이 아니라면 booked[0] unbooked[0] 도착시간 비교해서 push
    
    booked, unbooked 둘 중 하나 리스트가 null이면 남은 리스트 사람 순차적으로 push
    '''
    
    bi = 0
    ubi = 0
    
    name_list = [] # 업무 처리 순서가 정해진 사람의 이름 리스트
    time_list = [] # 각 사람들의 실제 업무 처리 시작 시간
    ti = 0 # booked, unbooked 비교할 때 참고할 시간의 index값
    
    while True:
        
        if bi == len(booked):
            for i, v in unbooked[ubi:]:
                name_list.append(v)
            break
            
        if ubi == len(unbooked):
            for i, v in booked[bi:]:
                name_list.append(v)
            break
        
        print('?? {}  {}  {}  {}'.format(bi, ubi, booked[bi], unbooked[ubi]))
        
        b_t_h, b_t_m = int(booked[bi][0][:2]), int(booked[bi][0][3:])
        ub_t_h, ub_t_m = int(unbooked[ubi][0][:2]), int(unbooked[ubi][0][3:])
        
        print(b_t_h, b_t_m)
        print(ub_t_h, ub_t_m)
        
        # 업무처리 시간과 예약고객 도착 시간이 겹치는가?
        if time_list:
            t_h = int(time_list[ti][:2])
            t_m = int(time_list[ti][3:])
            
            if t_h*60+t_m <= b_t_h*60+b_t_m <= t_h*60+t_m+10:
                name_list.append(booked[bi][1])
                bi += 1
                if t_m+10 >= 60:
                    time_list.append("%d:%d"%(t_h+1, (t_m+10)%60 ))
                else:
                    time_list.append("%d:%d"%(t_h,t_m+10))
                print('!! time_list', time_list, '   name_list', name_list)
                continue
            else:
                if ti < len(time_list)-1: # time list의 마지막 원소가 아닐 때
                    ti += 1
                    continue
        
        # 업무처리 중이 아닐 때 booked와 unbooked 비교
        if b_t_h*60+b_t_m > ub_t_h*60+ub_t_m:
            name_list.append(unbooked[ubi][1])
            time_list.append(unbooked[ubi][0])
            ti = len(time_list)-1
            ubi += 1
            print('!!2 time_list', time_list, '   name_list', name_list)
        else:
            name_list.append(booked[bi][1])
            time_list.append(booked[bi][0])
            ti = len(time_list)-1
            bi += 1
            print('!!3 time_list', time_list, '   name_list', name_list)
            
    print('!!4 time_list', time_list, '   name_list', name_list)
    

    return name_list




print( solution([],[]) )

