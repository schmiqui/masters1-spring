
def simple_power(base, power, modulo):
    return (base ** power) % modulo

def power_modulo(base, power, modulo):
    res = []
    for i in range(power):
        res.append((base ** i) % modulo)
    return res

def halving_power(base, power, modulo):
    result = base
    base = base % modulo
    while power > 1:
        if power % 2 == 0:
            result **= 2
            power //= 2
        else:
            result *= base
            power -= 1
        result %= modulo
    return result

def halving_power_2(base, power, modulo):
    result = 1
    # base = base % modulo
    squares = base % modulo
    for bin_digit in bin(power)[2:][::-1]:
        if bin_digit == '1':
            result = (result * squares) % modulo
        squares = (squares * squares) % modulo
    return result


if __name__ == "__main__":
    print(halving_power_2(7, 84, 20))