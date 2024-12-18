number_list = [1,2,3,4,5,6]

for i in number_list:
    print(i)

elements = [1,2,3,4]
print("outside the loop")
for i in elements:
    print("loop is starting",i)

    if i % 2 == 0:
        print("number is divisible by 2!")
    if i % 3 == 0:
        print("number is divisible by 3!")
    if i == 1:
        print("number is 1!")
    print("loop is finished")
    print("outside the loop")