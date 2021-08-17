from math import pow


def isEven(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


isEven(9)


def cube(number):
    return pow(number, 3)


number = 3
result = cube(number)

print("cube of number " + str(number) + " is " + str(result))


print("====in operator====")


def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


ask_ok("Do you really want to quit?")
