from typing import List

def max_harvest_with_turns(grid: List[List[int]], K: int) -> int:
    N, M = len(grid), len(grid[0])
    max_productivity = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, up, down, right

    def is_border(i, j):
        return i == 0 or i == N - 1 or j == 0 or j == M - 1

    def dfs(i, j, dir_index, turns, total, visited):
        nonlocal max_productivity
        max_productivity = max(max_productivity, total)
        for new_index, (di, dj) in enumerate(directions):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                new_turns = turns + (1 if new_index != dir_index else 0)
                if new_turns <= K:
                    visited[ni][nj] = True
                    dfs(ni, nj, new_index, new_turns, total + grid[ni][nj], visited)
                    visited[ni][nj] = False

    for i in range(N):
        for j in range(M):
            if is_border(i, j):
                for dir_index, (di, dj) in enumerate(directions):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        visited = [[False for _ in range(M)] for _ in range(N)]
                        visited[i][j] = True
                        dfs(i, j, dir_index, 0, grid[i][j], visited)

    return max_productivity
