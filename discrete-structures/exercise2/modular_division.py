def gcdExtended(a, b):
    print(a,b)
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Compute modular inverse
def modInverse(b, M):
    gcd, x, _ = gcdExtended(b, M)
    print(gcd, x)
    if gcd != 1:
        return -1
    return (x % M + M) % M

# Perform (a / b) % M
def modDivide(a, b, M):
    print(a,b,M)
    a %= M
    inv = modInverse(b, M)
    if inv == -1:
        return -1
    return (a * inv) % M

if __name__ == "__main__":
    a = 345
    b = 6
    M = 109
    result = modDivide(a, b, M)
    print(result)