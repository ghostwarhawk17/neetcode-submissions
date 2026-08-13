class Solution:
    def search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                low = mid + 1        
            else:
                high = mid - 1
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)

        for i in range(row):          
            if self.search(matrix[i], target) != -1:  
                return True
        return False                    