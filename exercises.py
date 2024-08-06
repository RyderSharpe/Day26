# Square numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [square ** 2 for square in numbers]
# print(squared_numbers)

# Filter even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(inter) for inter in list_of_strings]
print(numbers)
# Create a new list containing only the even numbers
result = [number for number in numbers if number % 2 == 0]
print(result)