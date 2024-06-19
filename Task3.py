#Task3a

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 91},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95}
]

s_students = sorted(students, key=lambda x: x['score'], reverse=True)

print(1, s_students)

#Task3b

strings = ['data', 'science', 'python', 'comprehension', '3']

char_frequency = {}

for string in strings:
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

print(3, char_frequency)

