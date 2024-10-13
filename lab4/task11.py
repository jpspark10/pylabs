def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in roman[::-1]:
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total


def int_to_roman(number):
    value_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ''
    for value, numeral in value_map:
        while number >= value:
            roman += numeral
            number -= value
    return roman


def sum_roman_numbers(one, two):
    sum_value = roman_to_int(one) + roman_to_int(two)
    return int_to_roman(sum_value)


if __name__ == "__main__":
    one = "V"
    two = "IV"
    print(sum_roman_numbers(one, two))  # IX
