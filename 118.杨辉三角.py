class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        init_matrix = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp_line = [1] * (i+1)
            for j in range(1, len(tmp_line)-1):
                tmp_line[j] = init_matrix[i-1][j-1] + init_matrix[i-1][j]
            init_matrix.append(tmp_line)

        return init_matrix