# NASE POCITY PRI RIESENI ZADANIA https://www.youtube.com/watch?v=BJVyTY82H8A
# KED SME TO AKO TAK VYRIESILI https://www.youtube.com/watch?v=Sk0eQqP_d6c

DEFAULT_VALUE = -9999
VALID_SUBTRACT_CHARS = {"IV", "IX", "XL", "XC", "CD", "CM"}
MAX_LETTER_COUNT = {"I": 3, "V": 1, "X": 3, "L": 1, "C": 3, "D": 1, "M": 3}


def convertToInt(roman_number):
    numbers_mapper = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000
    }

    # CHECK TYPE AND EMPTY
    if not isinstance(roman_number, str) or not roman_number:
        return DEFAULT_VALUE

    # CORRECT LETTERS CHECK
    input_letters, valid_letters = set(roman_number), set(numbers_mapper.keys())
    union = input_letters | valid_letters
    if union != valid_letters:
        return DEFAULT_VALUE

    # V, L, D CAN ONLY APPEAR ONCE TOTAL
    for char in ("V", "L", "D"):
        if roman_number.count(char) > 1:
            return DEFAULT_VALUE

    # CORRECT SEQUENCE (consecutive repetition)
    count = 1
    last_char = roman_number[0]
    for i in range(1, len(roman_number)):
        char = roman_number[i]
        if char == last_char:
            count += 1
        else:
            count = 1
            last_char = char
        if count > MAX_LETTER_COUNT[char]:
            return DEFAULT_VALUE

    # COMPUTE VALUE AND VALIDATE ORDERING
    res = 0
    i = 0
    last_val = float('inf')
    after_pair = False
    used_subtractive_pairs = set()

    while i < len(roman_number):
        actual_letter = roman_number[i]
        next_letter = roman_number[i + 1] if i + 1 < len(roman_number) else None

        actual_value = numbers_mapper[actual_letter]
        next_value = numbers_mapper.get(next_letter, 0)

        if actual_value < next_value:
            pair = f"{actual_letter}{next_letter}"
            if pair not in VALID_SUBTRACT_CHARS:
                return DEFAULT_VALUE
            if pair in used_subtractive_pairs:
                return DEFAULT_VALUE

            val = next_value - actual_value
            if val > last_val:
                return DEFAULT_VALUE
            if after_pair and val == last_val:
                return DEFAULT_VALUE

            res += val
            last_val = actual_value
            after_pair = True
            used_subtractive_pairs.add(pair)
            i += 2

        else:
            if actual_value > last_val:
                return DEFAULT_VALUE
            if after_pair and actual_value >= last_val:
                return DEFAULT_VALUE

            res += actual_value
            last_val = actual_value
            after_pair = False
            i += 1

    return res
