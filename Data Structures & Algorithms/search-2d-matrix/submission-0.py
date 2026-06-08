class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            n = len(matrix[i])
            start = 0
            end = len(matrix[i]) - 1
            if (target <= matrix[i][end] and target >= matrix[i][start]):
                l = start
                r = end
                while(l <= r):
                    mid = l + (r - l) // 2
                    if (matrix[i][mid] == target):
                        return True
                    elif (matrix[i][mid] > target):
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                continue
        return False