class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int: 
        start = 0
        tank = gas[0] - cost[0]
        tank = 0
        circle = False
        for n in range(len(gas) * 2):
            if n < len(gas):
                pos = n
            else:
                pos = n - len(gas)
                circle = True
            tank += gas[pos]
            tank -= cost[pos]
            if tank < 0:  
                tank = 0
                if gas[pos] < cost[pos]:
                    start = pos + 1
                else:
                    start = pos  
                circle = False
            else:
                if pos == len(gas) - 1:
                    if start == 0:
                        if circle == True:
                            return start
                if pos + 1 == start:
                    if circle == True:
                        return start
        return -1