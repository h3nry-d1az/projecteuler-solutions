from functools import reduce

decipher = lambda txt, key: map(lambda p: ord(p[0])^ord(p[1]), zip(txt, key*485))
decipher.__doc__ = """Apply XOR decryption to the problem text with a given 3-letter password."""

def points(c: str) -> int:
    """Returns how plausible it is for `c` to be part of an English word."""
    if c in range(ord('a'), ord('z')+1): return 2
    if c in range(ord('A'), ord('Z')+1): return 1
    if chr(c) in {'(', ')', ' ', '\'', '"', '?', '!', '-', ',', '.'}: return 0
    return -5

validate = lambda txt: sum(points(c) for c in txt)
validate.__doc__ = """Apply `points` to the entire text and sum all points."""

def main(encrypted: str) -> int:
    """Solution entry point."""
    scores = []
    for a in (chr(i) for i in range(ord('a'), ord('z')+1)):
        for b in (chr(i) for i in range(ord('a'), ord('z')+1)):
            for c in (chr(i) for i in range(ord('a'), ord('z')+1)):
                scores.append((a+b+c, validate(decipher(encrypted, a+b+c))))
    return sum(decipher(encrypted, max(scores, key=lambda p: p[1])[0]))

if __name__ == '__main__':
    with open('0059_cipher.txt') as f:
        print(main(reduce(lambda a, b: a+b, map(lambda c: chr(int(c)), f.read().split(',')))))