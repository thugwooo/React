def cross(W, L, trucks):
    bridge = [0] * W
    time = 0
    while bridge:
        time += 1
        bridge.pop(0)
        if trucks:
            if sum(bridge) + trucks[0] <= L:
                bridge.append(trucks.pop(0))
            else:
                bridge.append(0)

    return time

N, W, L = map(int, input().split())
trucks = list(map(int,input().split()))
answer = cross(W,L,trucks)
print(answer)