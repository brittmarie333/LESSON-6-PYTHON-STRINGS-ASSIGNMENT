#Objective: The aim of this assignment is to process and format user input data.
#Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

firstName = input("What's your first name? ")
lastName = input("What's your last name? ")

name = firstName +  lastName

name_length = name.length   

print(F"The lenght of your name is: " )