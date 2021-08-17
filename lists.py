states = ["Andhra", "Karnataka", "Tamilnadu", 5]

print(states)

states[2] = "TN"
print(states[1:])

scores = [1, 2, 3, 5]
states.append("Delhi")
states.extend(scores)
print(states)
print(states.index(5))


pair = (1, 2)
print(pair)
print(pair[0])