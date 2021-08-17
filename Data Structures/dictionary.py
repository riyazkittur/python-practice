data_quality = {0: "Good", 1: "Bad", 2: "Freeze", 3: "Alarm"}

data_quality[4] = "Average"


for k, v in data_quality.items():
    print(k, v)

print(data_quality[0])

print(data_quality.get(1))

print(data_quality.get(8))

print(data_quality.get(8, "Not a valid quaity bit"))

# print(data_quality[8])

print(data_quality.values())

print(data_quality.keys())

data_quality.pop(3)
print("Data after pop")
print(data_quality)

data_quality.popitem()
print("Data after pop item")
print(data_quality)
data_quality[1] = "Very Bad"
print(data_quality)
