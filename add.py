def is_flat(lst):
    return all(isinstance(item, int) for item in lst)

def simplify(lst):
    if not isinstance(lst, list):
        return lst
    if is_flat(lst) and len(set(lst)) == 1:
        return lst[0]
    return [simplify(item) for item in lst]

def add(s1, s2):
    if isinstance(s1, int) and isinstance(s2, int):
        return s1 + s2
    if isinstance(s1, int):
        s1 = [s1] * 4
    if isinstance(s2, int):
        s2 = [s2] * 4
    return simplify([add(a, b) for a, b in zip(s1, s2)])

def run_test(s1, s2, expected):
    result = add(s1, s2)
    assert result == expected, f"Test failed: add({s1}, {s2}) = {result}, expected {expected}"

# Test cases
run_test(0, 1, 1)
run_test(0, [1, 0, 1, 0], [1, 0, 1, 0])
run_test([0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 2])
run_test([0, [1, 1, 1, 1], [0, 0, 0, 0], 1], [1, [1, 0, 1, 1], [1, 0, 1, 0], 1], [1, [2, 1, 2, 1], [1, 0, 1, 0], 2])
run_test([0, [1, 1, 1, 0], [0, 0, 0, 0], 1], [1, [1, 0, 1, 1], [1, 0, 1, 0], 1], [1, [2, 1, 2, 1], [1, 0, 1, 0], 2])
run_test([0, [1, 1, 1, 1], [0, 0, 0, 0], 1], [1, [1, 0, 1, [0, 0, 0, 0]], [1, 0, 1, 0], 1], [1, [2, 1, 2, [0, 0, 0, 0]], [1, 0, 1, 0], 2])

print("All tests passed!")



