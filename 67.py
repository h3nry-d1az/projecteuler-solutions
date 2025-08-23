from typing import List

def main(triangle: List[List[int]]) -> int:
    """Solution entry point."""
    max_array = [[0]*len(r) for r in triangle]
    max_array[0][0] = triangle[0][0]
    for i, r in enumerate(triangle):
        if i == 0: continue
        for j, e in enumerate(r):
            max_array[i][j] = e + max(max_array[i-1][j] if j != len(r) - 1 else 0, max_array[i-1][j-1] if j != 0 else 0)
    return max(max_array[-1])

if __name__ == '__main__':
    triangle = []
    with open('triangle.txt', 'r') as f:
        triangle = [list(map(int, l.split())) for l in f.read().splitlines()]
    print(main(triangle))