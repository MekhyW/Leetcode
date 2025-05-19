# 🚜 Max-Harvest with Limited Turns

## Problem

This problem is a harder variant of the ["Worm Field"](https://www.beecrowd.com.br/repository/UOJ_2293.html) problem originally created for Brazilian Informatics Olympiad 2005 (OBI 2005).

An experimental farm is divided into a rectangular grid of N rows and M columns, where each cell contains an integer representing the productivity of that cell in earthworm units. A harvesting machine collects worms by moving across this grid.

The machine can:

- Start at any cell on the border of the field.

- Move one cell at a time in any of the four cardinal directions (up, down, left, right).

- Make at most K turns (where a turn is defined as a change in movement direction).

- Collect productivity values from each visited cell.

- Cannot revisit any cell.

- Must exit at another border cell.

Write a function to compute the maximum total productivity that the machine can harvest in a single pass that obeys the above rules.

---

## Examples

### Example 1

**Input:**

```python
grid = [
  [2, 4, 1],
  [3, 10, 1],
  [2, 1, 5]
]
K = 1
```

**Output:**

```python
16
```

---

### Example 2

**Input:**

```python
grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
K = 2
```

**Output:**

```python
29
```

---

## Restrictions

* `1 <= N, M <= 100`
* `0 <= grid[i][j] <= 10`
* `0 <= K <= min(N, M)`

---

## Tips

1) You can use BFS or DFS with a state that tracks: (i, j, direction, turns_used).
2) Use a priority queue to maximize the productivity at each step.
3) Be careful to avoid revisiting the same cell.
4) Consider precomputing all valid starting positions on the border.

---

## Pseudocode Solution

```sql
Function max_harvest_with_turns(grid, K):
    Initialize N, M from grid dimensions
    directions = [UP, DOWN, LEFT, RIGHT]

    Define function is_border(i, j):
        Return True if (i, j) is on the border of the grid

    Initialize max_productivity = 0

    For each cell (i, j) in the grid:
        If is_border(i, j):
            For each direction d in directions:
                Call DFS(i, j, d, 0, grid[i][j], visited)

    Function DFS(i, j, direction, turns, total, visited):
        Update max_productivity if total is greater
        For each possible new_direction in directions:
            Compute next_i, next_j from direction
            If cell is in bounds and not visited:
                If new_direction != direction:
                    If turns + 1 > K: skip
                    Else: increment turns
                Mark (next_i, next_j) visited
                DFS(next_i, next_j, new_direction, turns, total + grid[next_i][next_j], visited)
                Unmark (next_i, next_j) visited

    Return max_productivity
```

---

## Follow-up

### 1. What if the machine could revisit cells but not collect from them again?

### 2. What if the machine could only turn at certain marked cells?
