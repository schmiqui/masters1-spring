def euclidian(a, b):
    a, b = abs(a), abs(b)
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        return euclidian(a, b - a)

    return euclidian(a - b, b)

def test_euclidian():
    assert euclidian(35, 56) == 7
    assert euclidian(74, 29) == 1
    assert euclidian(0, 5) == 5
    assert euclidian(5, 0) == 5
    assert euclidian(10, 10) == 10
    assert euclidian(-24, 18) == 6
    assert euclidian(24, -18) == 6
    assert euclidian(-24, -18) == 6

    assert euclidian(21, 6) == euclidian(6, 21)
    assert euclidian(48, 18) == 6

test_euclidian()
print("All tests passed!")