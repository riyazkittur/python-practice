def printNumbers(i):
    while i <= 10:
        print(i)
        i = i - 1
        if i == 7:
            return
    print("End of loop")


printNumbers(10)