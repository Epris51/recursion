def validate(s):
    """Validate that a given square is valid."""

    # Check if it's a simple square
    if isinstance(s, int):
        return s in [0, 1]

    # If it's not a list or doesn't have exactly four elements, it's invalid
    if not isinstance(s, list) or len(s) != 4:
        return False

    # Recursively validate each element in the list
    return all(validate(part) for part in s)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; THAT'S SUPER-VALID WORK!\n")

