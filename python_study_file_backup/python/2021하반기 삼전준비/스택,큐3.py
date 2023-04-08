from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    # 현재 다리 위 트럭 무게 합
    bridge_truck = [ 0 for _ in range(bridge_length) ]
    time = 0
    while True:
        time += 1
        bridge_truck.pop(0)
        
        if len(bridge_truck) == 0:
            break
        
        if len(truck_weights) > 0 :
            if (sum(bridge_truck) + truck_weights[0]) <= weight :
                bridge_truck.append(truck_weights.pop(0))
            else:
                bridge_truck.append(0)
        print("truck_weights : {} \nbridge_truck : {} \ntime : {}\nsum(bridge_truck) : {}\nlen(bridge_truck) : {}\n".format(truck_weights, bridge_truck, time, sum(bridge_truck), len(bridge_truck)))
            
 #       else:
 #           bridge_truck.pop(0)
 #           if len(bridge_truck) == 0:
 #               time += bridge_length
 #           else :
 #               time += 1
 #       print("truck_weights : {} \nbridge_truck : {} \ntime : {}\nsum(bridge_truck) : {}\nlen(bridge_truck) : {}\n".format(truck_weights, bridge_truck, time, sum(bridge_truck), len(bridge_truck)))
    return time

def solution1(bridge_length, weight, truck_weights):
    time = 0
    bridge_truck = [ 0 for _ in range(len(bridge_length)) ]
    
    while len(bridge_truck):
        
        if truck_weights:
            if sum(bridge_truck) + truck_weights[0] <= weight:
                bridge_truck.append(truck_weights.pop(0))
    
    
    return time



b1 = 2
w1 = 10
t1 = [7,4,5,6]

b2 = 100
w2 = 100
t2 = [10]

b3 = 100
w3 = 100
t3 = [10,10,10,10,10,10,10,10,10,10]

b4 = 100
w4 = 50
t4 = [10,10,10,10,10,10,10,10,10,10]

#solution(b1, w1, t1)
print("\nTest1")
print(solution(b1, w1, t1))
#print("\nTest2")
#print(solution(b2, w2, t2))
#print("\nTest3")
#print(solution(b3, w3, t3))
#print("\nTest4")
#print(solution(b4, w4, t4))






