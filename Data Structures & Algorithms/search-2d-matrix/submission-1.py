class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j =  len(matrix[0])-1
        while i<len(matrix) and matrix[i][j] < target:
            i += 1

        if i == len(matrix):
            return False
        
        left,right = 0,len(matrix[0])-1
        while left <= right:
            mid = (left + right)//2

            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
