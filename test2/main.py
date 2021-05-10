def num_generator(input, multiplier_a, multiplier_b):
    num2remove_a = int(input / multiplier_a)
    num2remove_b = int(input / multiplier_b)
    num2added = int(input / (multiplier_a * multiplier_b))
    result = input - num2remove_a - num2remove_b + 2*num2added
    print(result)
    return result


if __name__ == "__main__":
    while True:
        a = int(input())
        b = int(input())
        c = int(input())
        num_generator(a, b, c)