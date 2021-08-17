fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits[1])

print(fruits.count("apple"))

print(fruits.index("apple"))
fruits.append("dragon fruit")
print(fruits)
fruits.sort()
print(fruits)
print(set(fruits))
num = [1, 2, 3]

fruits.extend(num)
print(fruits)

students = [(1, "A"), (2, "Z"), (3, "B")]

# sort list with second element in the pair
students.sort(key=lambda pair: pair[1])

print(students)

numbers = [10, 20, 30, 40]

for i, v in enumerate(numbers):
    print(i, v)
