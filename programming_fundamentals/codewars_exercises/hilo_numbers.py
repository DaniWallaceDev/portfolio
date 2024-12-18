def high_and_low(numbers):
    numbers = sorted([int(i) for i in numbers.split(" ")])
    return f"{numbers[len(numbers) - 1]} {numbers[0]}"


print(high_and_low("1 2 4 9 2 4 1 2"))


def high_and_low(numbers):
    numbers = numbers.split(" ")
    n = []
    for i in numbers:
        n.append(int(i))
    order_n = sorted(n)
    return f"{order_n[-1]} {order_n[0]}"


print(high_and_low("1 4 3 2"))

