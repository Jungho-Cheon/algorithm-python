def solution(bridge_length, weight, truck_weights):
    bridge_weight = 0

    Q = []
    done = []
    trucks = len(truck_weights)
    time = 0
    while(len(done) < trucks):
        if Q:
            if(Q[0][0] == time):
                print("time : {}, pop : {}".format(time, Q[0][1]))
                tmp = Q.pop(0)
                done.append(tmp)
                bridge_weight -= tmp[1]

        if truck_weights:
            if(bridge_weight + truck_weights[0] <= weight):
                print("time : {}, insert : {}".format(time, truck_weights[0]))
                Q.append((time + bridge_length, truck_weights[0]))
                bridge_weight += truck_weights.pop(0)

        time += 1

    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
