import sympy

def modular_addition(a, b, modulo):
    a_mod = a % modulo
    b_mod = b % modulo
    return (a_mod + b_mod) % modulo

def modular_subtraction(a, b, modulo):
    a_mod = a % modulo
    b_mod = b % modulo
    return (a_mod - b_mod) % modulo

def modular_multiplication(a, b, modulo):
    a_mod = a % modulo
    b_mod = b % modulo
    return (a_mod * b_mod) % modulo

def modular_division(a, b, modulo):
    g, x, y = extended_euclidean_algorithm(b, modulo)
    if g != 1:
        return ValueError("division is not defined because b has no modular inverse under this modulo")
    return (x * a) & modulo

def modular_power(base, power, modulo):
    result = 1
    squares = base % modulo
    for bin_digit in bin(power)[2:][::-1]:
        if bin_digit == '1':
            result = (result * squares) % modulo
        squares = (squares * squares) % modulo
    return result

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b, print_process=False):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_euclidean_algorithm(b, a % b, print_process)
    x = y1
    y = x1 - (a // b) * y1
    if print_process:
        if y >= 0:
            print(f'{g} = {x}.{a} + {y}.{b}')
        else:
            print(f'{g} = {x}.{a} - {abs(y)}.{b}')
    return g, x, y

def euler_totient(n):
    unique_prime_factors = set(prime_factors(n))
    res = n
    for prime_factor in unique_prime_factors:
        res *= (1 - (1 / prime_factor))
    return int(res)

def prime_factors(n):
    primes = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 1
    if n > 1:
        primes.append(n)
    return primes

def prime_factors_sym(n):
    return sympy.ntheory.factorint(n)

def euler_totient_sym(n):
    return sympy.totient(n)

def print_modular_multiplication_table(modulo):
    numbers = list(range(1, modulo))

    print("  |", *numbers)
    print("--+" + "---" * len(numbers))

    for a in numbers:
        row = [(a * b) % modulo for b in numbers]
        print(a, "|", *row)

def print_modular_addition_table(modulo):
    numbers = list(range(1, modulo))

    print("  |", *numbers)
    print("--+" + "---" * len(numbers))

    for a in numbers:
        row = [(a + b) % modulo for b in numbers]
        print(a, "|", *row)


if __name__ == "__main__":
    # print(extended_euclidean_algorithm(49, 87, print_process=True))
    # print(modular_division(6, 11, 87))
    # print(modular_multiplication(12334, 56789, 10))
    # print(euler_totient(45632))
    # print(euler_totient_sym(45632))
    # print(prime_factors(100000))
    # print(prime_factors_sym(100000))
    # print_modular_multiplication_table(6)
    # print_modular_addition_table(6)

    print()