class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy
        if sum(gas) < sum(cost):
            return -1
        current_tank_balance = 0
        start_index = 0
        for i in range(len(gas)):
            current_tank_balance += gas[i] - cost[i]
            if current_tank_balance < 0:
                current_tank_balance = 0
                start_index = i + 1
        return start_index



        