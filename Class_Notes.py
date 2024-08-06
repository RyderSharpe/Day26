LIST COMPREHENSION: Create a new list from a previous list.

BOTH EXAMPLES PRODUCE THE SAME OUTPUT
######################################################
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
######################################################

name = "Ryder"
new_list = [letter for letter in name]
# OUTPUT: ['R', 'y', 'd', 'e', 'r']
######################################################

# CONDITIONAL LIST COMPREHENSION
result = [NAMED_ANYTHING for NAMED_ANYTHING in numbers if NAMED_ANYTHING % 2 == 0]
new_list = [new_item for item in list if test] # Item can be called anything you want

names = ["Alex","Joe","Roger","PeterMcPeterson"]
# new_list = [name for name in names if len(name) < 5]
newlist = [nom.upper() for nom in names if len(nom) < 5]
print(newlist)
######################################################

new_list = [new_item for item in list if test]
new_list = [SAME_NAME for SAME_NAME in list if SAME_NAME]

Here’s what each part does:

1. new_item: This is the expression that defines what each element of the new list will be. It can be any expression involving item.
2. item: This is a variable that takes each value from the iterable (e.g., list) one by one.
3. list: This is the iterable (e.g., a list) that you are iterating over.
4. test: This is an optional condition (a boolean expression). Only items for which this condition evaluates to True are included in the new list.
    
What Can Be in Each Place:
new_item: Any expression that can use item. It can be a calculation, a function call, a transformation, etc. Example: number**2, str(item), item * 2, item.upper().
item: Any variable name that you use to represent each element of the iterable. This name should be used consistently within the comprehension.
list: Any iterable (e.g., list, tuple, set, dictionary keys or values, string).
test: Any boolean expression that can use item. This is optional, and if omitted, all items from the iterable are included. Example: item % 2 == 0, len(item) > 3, item.startswith('A').







    
