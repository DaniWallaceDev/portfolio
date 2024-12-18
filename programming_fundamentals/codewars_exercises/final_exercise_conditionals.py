books = {
    "don quijote": True,
    "twelve rules for life": True,
    "atomic habits": True,
    "sophies choice": True
}
while True:
    user_input: str = input("")
    user_input = user_input.lower()


    if user_input in books and books[user_input]:
        print("book is available")
        books[user_input] = False

    else:
        if "return" in user_input:
            user_input = user_input.replace("return", "").strip()
            if not books[user_input]:
                books[user_input] = True
        else:
            print(f"{user_input} is unavailable")


## write your code here
