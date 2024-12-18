def make_negative(number):
    if number > 0:
        return -number
    else:
        return number

number = int(input("Enter a number: "))
result = make_negative(number)
print(f"Number {number} converted to negative is: {result}")

# Es mejor multiplicar por -1 que colocar el simbolo de - refactorizar esto
