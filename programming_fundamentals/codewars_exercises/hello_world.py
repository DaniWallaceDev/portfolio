print("helló there")
print('helló there')

l1 = [22, "sleep", 'culo']


# Python3 code to demonstrate
# interlist element concatenation
# using list comprehension + zip()

# initializing lists
test_list1 = ["Geeksfor", "i", "be"]
test_list2 = ['Geeks', 's', 'st']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using list comprehension + zip()
# interlist element concatenation
res = test_list1 + test_list2

# printing result
print("The list after element concatenation is : " + str(res))