r"""# Lattice Paths
## Problem Statement
Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.

<div align="center"><img src="https://projecteuler.net/resources/images/0015.png" class="dark_img" alt=""></div>

How many such routes are there through a $20 \times 20$ grid?

## Solution
A good strategy to attack these self-repeating, bifurcation problems is through recursion.

It is known that whenever we have moved a total of $n$ times either down or to the right -- where $n$ is the size of the grid -- there is only one way to go (because we can no longer move in that direction), so the number of paths in that scenario is $1$, that would be our base case. Likewise, in any other inner state, the number of paths would be the sum of those when moving one unit to the right plus the same downwards.

Overall, we could implement this algorithm as a Python one-liner as `count_paths=lambda n,x,y: 1 if x==n or y==n else count_paths(n,x+1,y)+count_paths(n,x,y+1)`, although it would be genuinely inefficient since useless recalculations would be performed. Thus, memoization turns out to be a very useful optimization technique in this solution.

Finally, after a short execution the procedure described above yields $\boxed{137846528820}$."""

__memo = {}
def count_paths(n: int, x: int = 0, y: int = 0) -> int:
  r"""Counts the number of paths in an $n\times n$ grid from the top-left corner to the bottom-right one, where one can only move downwards and rightwards. The optional arguments $x$, $y$ indicate the starting position, where $(0,0)$ is the beginning vertex and $(n, n)$ is the ending one."""
  if x == n or y == n: return 1
  if (k := __memo.get((x, y))): return k
  __memo[(x, y)] = count_paths(n,x+1,y) + count_paths(n,x,y+1)
  return __memo[(x, y)]

def solution() -> None:
  """Solution entry point."""
  print(count_paths(20))

if __name__ == '__main__': solution()