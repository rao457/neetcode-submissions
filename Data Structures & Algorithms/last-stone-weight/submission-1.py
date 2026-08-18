class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while(len(stones) >= 2):
            heavy1 = heapq.heappop(stones)
            heavy2 = heapq.heappop(stones)
            if heavy1 == heavy2:
                continue
            else:
                heapq.heappush(stones, heavy1 - heavy2)
        if stones:
            return -stones[0]
        else:
            return 0