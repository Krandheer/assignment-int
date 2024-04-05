from typing import List


def is_valid(x, y, visited, grid):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or visited[x][y]:
        return False
    return True


def dfs(grid, visited, node):
    i, j = node
    visited[i][j] = True
    dire = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for l, m in dire:
        if is_valid(i + l, j + m, visited, grid):
            visited[i + l][j + m] = True
            dfs(grid, visited, (i + l, j + m))


def numIslands(grid: List[List[str]]) -> int:
    visited = []
    land = 0
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            temp.append(False)
        visited.append(temp)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                visited[i][j] = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and not visited[i][j]:
                land += 1
                dfs(grid, visited, (i, j))
    return land


# test
# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
# ]
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"],
# ]
# print(numIslands(grid))
