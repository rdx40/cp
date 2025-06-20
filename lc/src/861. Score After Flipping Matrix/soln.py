class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        for j in range(1, n):
            ones = 0
            for i in range(m):
                if grid[i][j] == 1:
                    ones += 1
            zeros = m - ones
            if zeros > ones:
                for i in range(m):
                    grid[i][j] ^= 1
        score = 0
        for i in range(m):
            row_val = 0
            for j in range(n):
                row_val = (row_val << 1) | grid[i][j]
            score += row_val
        return score
