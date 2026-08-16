class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW,COL = len(matrix),len(matrix[0])
        res = [[0] * ROW for _ in range(COL)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
                
        return res
        