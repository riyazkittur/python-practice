numbers = [1, 2, 3, 4]
sq_numbers = [x ** 2 for x in numbers]
print(sq_numbers)

odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]

all_numbers = [(x, y) for x in odd_numbers for y in even_numbers if x != y]
print(all_numbers)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

single_list = [num for row in vec for num in row]

print(single_list)
args = [3, 6]
print(list(range(*args)))
# transpose using zip
print(list(zip(*vec)))
