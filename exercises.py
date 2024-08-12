# SQUARE NUMBERS
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [square ** 2 for square in numbers]
print(squared_numbers)

/////////////////////////////////////////////////////

# FILTER EVEN NUMBERS
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(inter) for inter in list_of_strings]
print(numbers)
# Create a new list containing only the even numbers
result = [number for number in numbers if number % 2 == 0]
print(result)

///////////////////////////////////////////////////////////////////////////

# CREATE A DICTIONARY RESULT WITH WORD LENGTHS FROM THE GIVEN SENTENCE.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list = sentence.split()
print(list)
result = {number: len(number) for number in list}
print(result)

////////////////////////////////////////////////////////////////////////////

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Example: Generate random score for each student.
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Freddie']
import random
students_scores = {student: random.randint(1, 100) for student in names}

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Freddie']
students_scores = {student: random.randint(1,100) for student in names}
print(students_scores)
# passed = {new_key: new_value for (key, value) in dictionary.items() if value > 60}
passed = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed)
