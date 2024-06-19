#Task4a
strings = ['data', 'science', 'python', 'comprehension', '2']

unique_characters = {char for word in strings for char in word}

print(2, unique_characters)

#Task4b

strings = ['data', 'science', 'python', 'comprehension', '3']

char_frequency = {}

for string in strings:
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

print(3, char_frequency)