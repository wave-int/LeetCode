class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for l in range(len(matrix) // 2):
            for n in range(l + 1, len(matrix) - l - 1):
                matrix[l][n] = matrix[l][n] + matrix[n][len(matrix) - 1 - l]
                matrix[n][len(matrix) - 1 - l] = matrix[l][n] - matrix[n][len(matrix) - 1 - l]
                matrix[l][n] = matrix[l][n] - matrix[n][len(matrix) - 1 - l]

            for n in range(l + 1, len(matrix) - l - 1):
                matrix[n][l] = matrix[n][l] + matrix[l][len(matrix) - 1 - n]
                matrix[l][len(matrix) - 1 - n] = matrix[n][l] - matrix[l][len(matrix) - 1 - n]
                matrix[n][l] = matrix[n][l] - matrix[l][len(matrix) - 1 - n]

            for n in range(l + 1, len(matrix) - l - 1):
                matrix[n][l] = matrix[n][l] + matrix[len(matrix) - l - 1][n]
                matrix[len(matrix) - l - 1][n] = matrix[n][l] - matrix[len(matrix) - l - 1][n]
                matrix[n][l] = matrix[n][l] - matrix[len(matrix) - l - 1][n]

            n = len(matrix) - l - 1
            matrix[l][l] = matrix[l][l] + matrix[l][n]
            matrix[l][n] = matrix[l][l] - matrix[l][n]
            matrix[l][l] = matrix[l][l] - matrix[l][n]

            matrix[l][l] = matrix[l][l] + matrix[n][l]
            matrix[n][l] = matrix[l][l] - matrix[n][l]
            matrix[l][l] = matrix[l][l] - matrix[n][l]

            matrix[n][l] = matrix[n][l] + matrix[n][n]
            matrix[n][n] = matrix[n][l] - matrix[n][n]
            matrix[n][l] = matrix[n][l] - matrix[n][n]