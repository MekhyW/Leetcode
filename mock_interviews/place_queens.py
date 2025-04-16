def place_queens(n: int) -> list[list[int]]:
    result = []

    def is_valid(queens, row, col):
        for r in range(row):
            if queens[r] == col:
                return False
            if abs(queens[r] - col) == abs(r - row):
                return False
        return True
    
    def backtrack(row, current_placement):
        if row == n:
            result.append(current_placement[:])
            return
        for col in range(n):
            if is_valid(current_placement, row, col):
                current_placement[row] = col
                backtrack(row + 1, current_placement)

    initial_placement = [-1] * n
    backtrack(0, initial_placement)
    return result
