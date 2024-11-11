from typing import List

class Solution:
    def getTotalIsles(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c):
            # Base case: if out of bounds or the cell is water or already visited, stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            visited[r][c] = True  # Mark the current cell as visited
            
            # Explore all four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        island_count = 0
        
        # Traverse each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    # New island found, initiate DFS
                    dfs(r, c)
                    island_count += 1
        
        return island_count