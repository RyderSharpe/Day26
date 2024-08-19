import pandas

# ## EXAMPLE ##
# student_dict = {
#     "Student": ["Pete", "Jon", "Rog"],
#     "Score" : [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     print(index)
#     #Access row.student or row.score
#     pass

##################### NATO PROJECT ###########################################################

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"} ie dict comprehension

# Keyword Method with iterrows()

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# # Format
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary using dictionary comprehension
p_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Get user input and convert it to uppercase to match dictionary keys
user_input = input(str("Enter a string: ")).upper()

# for i in user_input:
#     b = p_dict.get(i)
#     print(b)

# Iterate through each letter in the user input
nato = [p_dict.get(i) for i in user_input]
print(nato)

##################################################################################################

# ########### CLASS VERSION######################################################################
#
# # TODO: Step 1
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(data.to_dict())
# phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# # print(phonetic_dict)
#
# # TODO: Step 2
# word = input("Ask user to enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)
# ##################################################################################################
