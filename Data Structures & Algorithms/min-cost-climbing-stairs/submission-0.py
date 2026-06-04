class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        prev = cost[0]
        curr = cost[1]

        for i in range(2, len(cost)):
            next_cost = cost[i] + min(prev, curr)

            prev, curr = curr, next_cost
        
        return min(prev, curr)