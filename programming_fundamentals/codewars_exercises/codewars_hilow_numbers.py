def high_and_low(numbers):
    numbers = sorted([int(i) for i in numbers.split(" ")])
    return f"{numbers[len(numbers)-1]} {numbers[0]}"
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))