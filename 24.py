from itertools import permutations
from functools import reduce

class Permutation(object):
    __data: list

    def __init__(self, permutation: list): self.__data = permutation
    def __lt__(self, other):
        for a, b in zip(self.__data, other.retrieve()):
            if a == b: continue
            if a > b: return False
            return True
        return False

    def retrieve(self) -> list: return self.__data
    def display(self) -> str: return reduce(lambda c1, c2: c1+c2, map(str, self.__data))

main = lambda n, k: sorted(map(Permutation, permutations(range(n))))[k-1].display()
main.__doc__ = """Solution entry point."""

if __name__ == '__main__': print(main(10, 1_000_000))