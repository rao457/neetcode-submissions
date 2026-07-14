class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        curr = []
        def dfs(index, remaining):
            if remaining == 0:
                ans.append(curr.copy())
                return
            if remaining < 0:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                
                curr.append(candidates[i])
                dfs(i+1, remaining - candidates[i])
                curr.pop()

        dfs(0, target)
        return ans