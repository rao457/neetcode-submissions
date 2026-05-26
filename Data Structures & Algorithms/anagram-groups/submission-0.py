class Solution:
    def getFreq(self, word: str) -> tuple:
        freq_list = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            freq_list[index] += 1
        return tuple(freq_list)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for word in strs:
            key = self.getFreq(word)
            freq[key].append(word)

        return list(freq.values())
    