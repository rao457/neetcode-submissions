class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        freq_list = list(freq.items())
        sorted_list = sorted(freq_list, reverse=True, key=lambda x: x[1])
        for i in range(k):
            result.append(sorted_list[i][0])
        return result