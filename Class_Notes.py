LIST COMPREHENSION: Create a new list from a previous list.

BOTH EXAMPLES PRODUCE THE SAME OUTPUT
//////////////////////////////////////////////////////////
# Example 1: Original way.
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# Example 2: Using list comprehension.
numbers = [1,2,3]
new_list = [operation for item in list] # How to use
new_list = [n + 1 for n in numbers] # Example
//////////////////////////////////////////////////////////

name = "Ryder"
new_list = [letter for letter in name]
# OUTPUT: ['R', 'y', 'd', 'e', 'r']
//////////////////////////////////////////////////////////

# CONDITIONAL LIST COMPREHENSION
result = [NAMED_ANYTHING for NAMED_ANYTHING in numbers if NAMED_ANYTHING % 2 == 0]
new_list = [new_item for item in list if test] # Item can be called anything you want

names = ["Alex","Joe","Roger","PeterMcPeterson"]
# new_list = [name for name in names if len(name) < 5]
newlist = [nom.upper() for nom in names if len(nom) < 5]
print(newlist)
//////////////////////////////////////////////////////////

new_list = [new_item for item in list if test]
new_list = [SAME_NAME for SAME_NAME in list if SAME_NAME]

Here’s what each part does:

1. new_item: This is the expression that defines what each element of the new list will be. It can be any expression involving item.
   new_item: The operation or transformation applied to item that defines what gets included in the new list.

2. item: This is a variable that takes each value from the iterable (e.g., list) one by one.
   item: Each element from the original list (or any iterable).

3. list: This is the iterable (e.g., a list) that you are iterating over.
   list: The list you are pulling from. 

4. test: This is an optional condition (a boolean expression). Only items for which this condition evaluates to True are included in the new list.
   test: A condition that must be true for the item to be included in the new list

 
What Can Be in Each Place:

new_item: Any expression that can use item. It can be a calculation, a function call, a transformation, etc. Example: number**2, str(item), item * 2, item.upper().
item: Any variable name that you use to represent each element of the iterable. This name should be used consistently within the comprehension.
list: Any iterable (e.g., list, tuple, set, dictionary keys or values, string).
test: Any boolean expression that can use item. This is optional, and if omitted, all items from the iterable are included. Example: item % 2 == 0, len(item) > 3, item.startswith('A').

#######################################################################################################################################################################################

DICTIONARY COMPREHENSION

New_dict = {new_key: new_value for item in list}
New_dict = {new_key: new_value for (key, value) in dict.items()}
New_dict = {new_key: new_value for (key, value) in dict.items() if test}


breaking it down:
new_key is the label on the box (the name of the thing).
new_value is the thing inside the box (the value or content).
When we create a new dictionary, we're making new boxes with labels (new_key) and putting things inside those boxes (new_value).
For example:
{name: age for (name, age) in people.items()}
name is the label on the box (the person's name).
age is the thing inside the box (the person's age).
We're taking the name and age from the original dictionary people and creating new boxes with the same labels (name) and things inside (age).


Example: Generate random score for each student.
    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Freddie']
    import random
    students_scores = {student: random.randint(1, 100) for student in names}

Example.
    import random
    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elenor', 'Freddie']
    students_scores = {student: random.randint(1,100) for student in names}
    print(students_scores)
    # passed = {new_key: new_value for (key, value) in dictionary.items() if value > 60}
    passed = {student: score for (student, score) in students_scores.items() if score > 60}
    print(passed)

Example.
    # CREATE A DICTIONARY RESULT WITH WORD LENGTHS FROM THE GIVEN SENTENCE.
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    list = sentence.split()
    print(list)
    result = {number: len(number) for number in list}
    print(result)

///////////////////////////////////////////////////////////////////////////

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(f"This is the Key: {key}")
    # print(f"This is the Value: {value}")
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through data frame
for (key, value) in student_data_frame.items():
    #Access index and row
    #Access row.student or row.score
    print(f"This is the Key: \n{key}")
    print(f"This is the Value: \n{value}")
    pass

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)

# Keyword Method with iterrows()
# {new_key: new_value for (key, value) in dic.items()}
# {new_key: new_value for (index, row) in df.iterrows()}

    
