def simplify(s):
    """Simplify a split square."""

    # If s is an integer (simple square), return it as is
    if isinstance(s, int):
        return s

    # Simplify each element in the list
    simplified_elements = [simplify(element) for element in s]

    # If all elements are equal after simplification, return one of them
    if all(element == simplified_elements[0] for element in simplified_elements):
        return simplified_elements[0]

    # Otherwise, return the list as it is
    return simplified_elements


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; YOU MADE THAT SEEM SIMPLE!!\n")


