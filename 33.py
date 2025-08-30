from functools import reduce
from math import prod, gcd

def remove(c: str, s: str) -> str:
    """Remove the first occurence of `c` in `s`."""
    ls = list(s)
    try: ls.remove(c)
    except Exception: pass
    return reduce(lambda c1, c2: c1+c2, ls)

def main() -> int:
    """Solution entry point."""
    fractions = set()
    for d in range(11, 100):
        if d % 10 == 0: continue
        for n in range(10, d):
            sn, sd = str(n), str(d)
            for k in sd:
                rn = int(remove(k, sn))
                rd = int(remove(k, sd))
                if n*rd == rn*d: fractions.add((rn,rd))
    frac = (prod(map(lambda p: p[0], fractions)), prod(map(lambda p: p[1], fractions)))
    return frac[1]//gcd(frac[0], frac[1])

if __name__ == '__main__': print(main())