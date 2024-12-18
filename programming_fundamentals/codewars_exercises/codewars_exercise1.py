def get_count(sentence):
    count = 0
    vowels= ["a","e","i","o","u"]
    for char in sentence:
        if char in vowels:
            count= count + 1
    return count

print(get_count("cacota"))
