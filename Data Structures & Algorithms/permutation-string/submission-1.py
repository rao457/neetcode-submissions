class Solution:
    def countFreq(self, part: str) -> List[int]:
        freq = [0] * 26
        for char in part:
            index = ord(char) - ord('a')
            freq[index] += 1
        return freq
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = self.countFreq(s1)
        wind_start = 0
        wind_end = len(s1) - 1
        while(wind_end < len(s2)):
            window = s2[wind_start: wind_end + 1]
            wind_freq = self.countFreq(window)
            if s1_freq == wind_freq:
                return True
            wind_start += 1
            wind_end += 1
        return False
