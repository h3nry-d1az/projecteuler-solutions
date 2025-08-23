def main() -> int:
    """Solution entry point."""
    tt = 10**10
    count = 1
    for _ in range(7830457):
        count *= 2
        if count > tt: count -= tt
    return (28433*count + 1) % tt

if __name__ == '__main__': print(main())