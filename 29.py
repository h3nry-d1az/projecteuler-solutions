main = lambda n: len(set(a**b for a in range(2, n+1) for b in range(2, n+1)))
main.__doc__ = """Solution entry point."""

if __name__ == '__main__': print(main(100))