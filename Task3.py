#Task3a

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 91},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95}
]

s_students = sorted(students, key=lambda x: x['score'], reverse=True)

print(1, s_students)
