for index in range(10):
    print(index)

for index in range(1, 10, 2):
    print(index)

for index in range(0, 10, 2):
    print(index)
print("======Loop list=====")
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(len(weekdays)):
    print(weekdays[i])

print("====loop dictionary=====")
data_quality = {0: "Good", 1: "Bad", 2: "Freeze", 3: "Alarm"}

for i in range(len(data_quality)):
    print(data_quality[i])

for key in data_quality.keys():
    print(data_quality[key])
