def search(number, students):
    if(number in students):
            print(f"{students[number][0]} {students[number][1]}")
    else:
        print("Not found")

n = int(input())
students = {}
for i in range(n):
    student = input().split()
    students.update({student[0] : (student[1], student[2])})

q = int(input())
for i in range(q):
    number = input().strip()
    search(number, students)
