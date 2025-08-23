def retrieve_days(month: int, year: int) -> int:
    """Get the number of days of a given month within a given year."""
    if month in {4, 6, 9, 11}: return 30
    elif month != 2: return 31
    else: return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28

def main() -> int:
    """Solution entry point."""
    days_elapsed = 2
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            days_elapsed = (days_elapsed + retrieve_days(month, year)) % 7
            if days_elapsed == 0: count += 1
    return count

if __name__ == '__main__': print(main())