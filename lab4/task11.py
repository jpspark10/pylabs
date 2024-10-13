def int_to_roman(number):
    value_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    romanresult = ''
    for value, numeral in value_map:
        while number >= value:
            romanresult += numeral
            number -= value
    return romanresult


def roman():
    print(f'{int_to_roman(one)} + {int_to_roman(two)} = {int_to_roman(one + two)}')


if __name__ == "__main__":
    one = 5
    two = 4
    roman()
