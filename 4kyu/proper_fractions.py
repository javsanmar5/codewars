def proper_fractions(n: int) -> int:
    i = 1
    res = 0

    while i < n:
        if is_reduced(i, n): res += 1
        i += 1
    
    return res


def is_reduced(numerator: int, denominator: int) -> bool:
    gcd = find_gcd(numerator, denominator)
    return gcd == 1

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
x


print(proper_fractions(12))