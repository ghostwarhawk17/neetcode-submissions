class Solution:
   
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # set to keep track of positions with zero value
        hashmap_row = set()
        hashmap_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    hashmap_row.add(i)
                    hashmap_col.add(j)


        def makezero():
            for key in hashmap_row:
                for j in range(len(matrix[0])):
                    matrix[key][j] = 0

            for key in hashmap_col:
                for i in range(len(matrix)):
                    matrix[i][key] = 0

        makezero()
        


        

        

        