print(set([1, 2, 3, 1, 2, 3, 1]))

basket = {"apple", "banana", "apple", "mango", "papaya"}

print(basket)

if "apple" in basket:
    print("apple is already added to basket")

a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)

print(a | b)

print(a & b)

print(a ^ b)

c = set()

c = set("aba")
print(c)
print("===set_comprehension===")
set_comprehension = {x for x in "banana" if x not in "ab"}

print(set_comprehension)
