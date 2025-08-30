def to_binary_string(n: int) -> list:
    """Converts a number to a list of its binary digits."""
    s = []
    while n != 0:
        s.append(n & 1)
        n >>= 1
    return s

main = lambda: sum(i for i in range(1, 1000000) if (si:=str(i)) == si[::-1] and (bi:=to_binary_string(i)) == bi[::-1])
main.__doc__ = """Solution entry point."""

if __name__ == '__main__': print(main())