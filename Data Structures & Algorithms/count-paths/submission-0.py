class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = {} #cell : #of paths

        def dfs(row, column):
            if row == m-1 and column == n-1:
                return 1
            if (row, column) in visited:
                return visited[(row, column)]
            if row >= m or column >=n:
                return 0
            visited[(row, column)] = dfs(row, column + 1) + dfs(row + 1, column)
            return dfs(row, column + 1) + dfs(row + 1, column)
        return dfs(0, 0)