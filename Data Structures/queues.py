from collections import deque

queue = deque(["Riyaz", "Mrutyu", "Manju"])

queue.append("venkat")
queue.append("Ravi")
print(queue)
queue.popleft()
queue.popleft()

print(queue)