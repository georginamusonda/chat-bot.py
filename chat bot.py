
def new_func():
    name = input("What is your name? ")

    print("Hello", name + "! Nice to meet you.")

    feeling = input("How are you feeling today? ")

    if feeling.lower() == "good":
        print("That's great to hear! Keep smiling, " + name + "!")

new_func()
