class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())
        count_max = list(freq.values()).count(max_freq)

        result = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), result)