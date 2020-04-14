from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    self.dfs(i, j, visited, m, n, grid)
        return count

    def dfs(self, i, j, visited, m, n, grid):
        # 首先是个合法的点 其次得是岛 才能访问  再者得是没有访问过的才能继续扩散
        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == '1':
            if visited[i][j] == 0:
                visited[i][j] = 1
                self.dfs(i+1, j, visited, m, n, grid)
                self.dfs(i, j+1, visited, m, n, grid)
                self.dfs(i-1, j, visited, m, n, grid)
                self.dfs(i, j-1, visited, m, n, grid)


if __name__ == "__main__":
    x = Solution()
    re = x.numIslands([['1', '1'], ['1', '1'],['0','0'],['1','1']])
    print(re)
