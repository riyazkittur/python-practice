from Student import Student

student1 = Student("Riyaz", "Ahmed", 3.1)
student2 = Student("Sami", "Ahmed", 3.5)
if student1 == student2:
    print("Both are same")


students = [student1, student2]

for s in students:
    print(s.firstName)