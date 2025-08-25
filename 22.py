position = lambda c: ord(c) - ord('A') + 1
position.__doc__ = """Returns the position of `c` in the alphabet."""

main = lambda names: sum((i+1)*sum(map(position, name)) for i, name in enumerate(names))
main.__doc__ = """Solution entry point."""

if __name__ == '__main__': print(main(sorted(map(lambda n: n[1:-1], open('names.txt').read().split(',')))))