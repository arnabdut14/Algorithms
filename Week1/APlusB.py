# python3


def sum_of_two_digits(numbers):
    return numbers[0] + numbers[1]

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(sum_of_two_digits(input_numbers ))