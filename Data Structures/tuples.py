tuple = 1, 2, "Hello"
print(tuple)

print(tuple[1])

# tuples are immutable

# tuple[2] = "Hi"
num1, num2, message = tuple

print(num1, " ", num2, " ", message)


tuple = ([1, 2], [3, 4])
print(tuple)


singleton = ("riyaz",)

print(len(singleton))

x = [num for row in tuple for num in row if num > 2]

print(x)