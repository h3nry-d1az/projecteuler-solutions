from functools import reduce

def digit_writeout(d: int) -> str:
    """Writes out $d$, where $d$ ranges from $1$ to $9$."""
    match d:
        case 0: return ''
        case 1: return 'one'
        case 2: return 'two'
        case 3: return 'three'
        case 4: return 'four'
        case 5: return 'five'
        case 6: return 'six'
        case 7: return 'seven'
        case 8: return 'eight'
        case 9: return 'nine'

def tens_writeout(n: int) -> str:
    """Writes out $n$, where $n$ ranges from $1$ to $99$."""
    if n < 10: return digit_writeout(n)
    if n == 10: return 'ten'
    if n == 11: return 'eleven'
    if n == 12: return 'twelve'
    if n == 13: return 'thirteen'
    if n == 14: return 'fourteen'
    if n == 15: return 'fifteen'
    if n == 16: return 'sixteen'
    if n == 17: return 'seventeen'
    if n == 18: return 'eighteen'
    if n == 19: return 'nineteen'
    d = n % 10
    match n - d:
        case 20: return 'twenty'+digit_writeout(d)
        case 30: return 'thirty'+digit_writeout(d)
        case 40: return 'forty'+digit_writeout(d)
        case 50: return 'fifty'+digit_writeout(d)
        case 60: return 'sixty'+digit_writeout(d)
        case 70: return 'seventy'+digit_writeout(d)
        case 80: return 'eighty'+digit_writeout(d)
        case 90: return 'ninety'+digit_writeout(d)

def writeout(n: int) -> str:
    """Writes out $n$, where $n$ ranges from $1$ to $1000$."""
    if n < 100: return tens_writeout(n)
    if n == 100: return 'onehundred'
    if n == 1000: return 'onethousand'
    t = n % 100
    if t == 0: return digit_writeout((n-t)//100)+'hundred'
    return digit_writeout((n-t)//100)+'hundredand'+tens_writeout(t)

main = lambda: len(reduce(lambda a, b: a+b, (writeout(n) for n in range(1, 1001))))
main.__doc__ = """Solution entry point."""

if __name__ == '__main__': print(main())