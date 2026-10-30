class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #get the rotten bananas first
        q = collections.deque()
        seen = set()
        time = 0
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == 2:
                    q.append((row, column))
                    seen.add((row, column)) 
        rounds = len(q)
        while q:
            rounds -= 1
            row, column = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] #up down, right, left

            for dr, dc in directions:
                r, c = row + dr, column + dc
                if (r in range(rows) and
                    c in range(cols) and
                    (r, c) not in seen and
                    grid[r][c] == 1):
                    q.append((r, c))
                    grid[r][c] = 2
            if rounds == 0:
                if q:
                    time += 1
                rounds = len(q)
                      


        #check for healthy bananas
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == 1:
                    return -1
        return time
        
        
        