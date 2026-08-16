class Solution:
    def reverse(self,arr):
        l = 0
        r = len(arr) - 1
        while l <= r:
            arr[l],arr[r] = arr[r],arr[l]
            l +=1
            r -=1
        return arr

    def rotate(self, matrix: List[List[int]]) -> None:
        ROW,COL = len(matrix),len(matrix[0])
        res = [[0] * ROW for _ in range(COL)]
        for i in range(ROW):
            for j in range(COL):
                res[j][i] = matrix[i][j]

        for i in range(len(res)):
            matrix[i] = self.reverse(res[i])

