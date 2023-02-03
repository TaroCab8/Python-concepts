"""
Given a circular list of gas stations, where we can go from a station i to the station i +1, and the last one goes bac to the first one, find the index pf the station from where we start to be able to traverse all the statios and fo back to the initial one without runnin out of gas.

Note that:
- We can only move forward
- The gas tank starts empty
- gas[i] represents the amount of gas at the station i
- cost[i] represents the cost to go from the station  to the next one
- The answer is guaranteed to be unique
- if the sation we're searching for doesn't exist return -1

"""
# O(n2) time complexity. O(1) space complexity.

def can_traverse(gas, cost, start):
    n = len(gas)
    remaining = 0
    i= start
    started = False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1) % n
    return True

def gas_station(gas, cost):
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1

le_gas = [1,5,3,3,5,3,1,3,4,5] 
le_cost =[5,2,2,8,2,4,2,5,1,2]
#worst case-scenario
worst_gas = [2,2,2,2,2,2,2,2,2,2] 
worst_cost =[1,1,1,1,1,1,1,1,1,50]
print(gas_station(worst_gas, worst_cost))

"""
if a station start reaches a negative amount at the index i, then all stations between start and i inclusive are invalid, we start again from i+1

"""
# Optimal solution: this version has O(n) time complexity and O(n) space complexity
def gas_station_2(gas, cost):
    remaining = 0
    candidate = 0
    for i in range (len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i + 1
            remaining = 0
            prev_remaining = sum(gas[:candidate])-sum(cost[:candidate])
            remaining = 0
    if candidate == len(gas) or remaining + prev_remaining < 0:
        return -1
    else:
        return candidate

print(gas_station_2(le_gas, le_cost))