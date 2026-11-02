class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        rows, cols = len(grid), len(grid[0])
        turns = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

        indicator = len(queue)
        visited = set()
        while queue:
            row, col = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for r, c in directions:
                dr, dc = row+r, col+c
                if dr not in range (rows) or dc not in range(cols):
                    continue
                if grid[dr][dc] == 1 and (dr, dc) not in visited:
                    queue.append((dr, dc))
                    visited.add((dr, dc))
                    grid[dr][dc] = 2
            indicator -=1
            if indicator == 0:
                indicator = len(queue)
                turns += 1
                
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        if turns == 0:
            return 0
        else:
            return turns-1


        