def disemvowel(string_):
    vowels = "aeiouAEIOU"

    for i in vowels:
        string_ = string_.replace(i,'')

    return print(string_)
disemvowel("Me llamo pAco")