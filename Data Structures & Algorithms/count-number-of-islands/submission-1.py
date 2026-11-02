class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, column):
            queue = collections.deque()
            queue.append((row, column))
            visited.add((row, column))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                curr_r, curr_c = queue.popleft()
                for r, c in directions:
                    dr = curr_r + r
                    dc = curr_c + c
                    if dr not in range(rows) or dc not in range(cols) or dr < 0 or dc < 0:
                        continue
                    if grid[dr][dc] == "1" and (dr, dc) not in visited:
                        queue.append((dr, dc))
                        visited.add((dr, dc))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands