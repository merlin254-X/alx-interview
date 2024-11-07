#!/usr/bin/python3
import sys


def print_solution(solution):
    """Print a solution as a list of [row, column] positions for queens."""
    print(solution)


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[]):
    """Recursive function to solve the N queens problem using backtracking."""
    if row == n:
        print_solution(queens)
        return
    for col in range(n):
        if is_safe(queens, row, col):
            solve_nqueens(n, row + 1, queens + [[row, col]])


def main():
    # Check argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve N Queens
    solve_nqueens(n)


if __name__ == "__main__":
    main()
