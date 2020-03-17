ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
thousands = ["", "thousand", "million", "billion", "trillion"]


def parse_thousand(number: int):
    third_digit = number % 10
    number //= 10
    second_digit = number % 10
    number //= 10
    first_digit = number % 10
    number //= 10
    first_string: str = ""
    second_string: str = ""
    third_string: str = ""
    if first_digit != 0:
        first_string = f'{ones[first_digit]}hundred '
        if second_digit != 0 or third_digit != 0:
            second_string = 'and '
    if second_digit == 1:
        third_string = ones[10 * second_digit + third_digit]
    elif second_digit > 1:
        third_string = twenties[second_digit] + ones[third_digit]
    return f'{first_string}{second_string}{third_string}'


def say_the_number(number: int):
    if number == 0:
        return 'Zero'
    number_parts = []
    while number > 0:
        number_parts.append(number % 1000)
        number //= 1000
    result: list = []
    for idx, value in enumerate(number_parts):
        if value not in (0, 1):
            result.append(f'{parse_thousand(value)}{thousands[idx]}')
        elif value == 1:
            result.append(f'one {thousands[idx]}')
    return ", ".join(reversed(result)).capitalize()[:-1] + '.'


if __name__ == '__main__':
    tests = [0, 11, 1043283, 90376000010012]
    for test in tests:
        print(f'{test} -> {say_the_number(test)}')
