# ---------------------------------------------------------------------- #
# These two functions are optional, but may prove useful in computation: |
# ---------------------------------------------------------------------- #
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

def euler_phi(n: int) -> int:
    """Evaluates the Euler's phi function on input n."""
    unique_prime_factors = set(prime_factors(n))
    res = n
    for prime_factor in unique_prime_factors:
        res *= (1 - (1 / prime_factor))
    return int(res)


def simple_power(base: int, power: int, modulo: int) -> int:
    """Computes the value of: base^power (mod modulo)."""
    return pow(base, power, mod=modulo)



# ----------------------------------------------------------------------#
#           This is the proper function you should implement.           |
# You are free to use the above functions too - if you implement them - |
#       as well as any other functions you think will be helpful.       |
# ----------------------------------------------------------------------#


def power_tower(number: int, tower_height: int, base_modulo: int) -> int:
    """Computes the value of the power tower:
    number ^^ tower_height (mod base_modulo)"""
    if base_modulo == 1:
        return 0
    if tower_height == 0:
        return 1
    if tower_height == 1:
        return number % base_modulo
    if base_modulo == 2:
        return number % 2
    new_modulo = euler_phi(base_modulo)
    resp = power_tower(number, tower_height - 1, new_modulo)
    return simple_power(number, resp, base_modulo)


if __name__ == "__main__":
    # Below are the test cases to submit, replace the comments with answers:
    print(power_tower(7, 5, 10))  # 3
    print(power_tower(37, 13, 24))  # 13
    print(power_tower(7, 77, 100))  # 43
    print(power_tower(97, 97, 2025))  # 187
    print(power_tower(1707, 1783, 100000000))  # 40924243
    print(power_tower(1777, 1855, 100000000))  # 95962097
