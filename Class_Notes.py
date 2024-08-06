LIST CONDITIONAL: Create a new list from a previous list.

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
new_list = [new_item for item in list if test] # Item can be called anything you want

names = ["Alex","Joe","Roger","PeterMcPeterson"]
# new_list = [name for name in names if len(name) < 5]
newlist = [nom.upper() for nom in names if len(nom) < 5]
print(newlist)
