from ayush_project.Text_Generator.app import *

starter = '''Let's start the first project the Text Generator using NLP.
In this project, we will use a corpus that contains the entire script of Game of Thrones. As the corpus will be used to "train" a probabilistic model that will predict the next word in a chain of words, the generated text will resemble the style and vocabulary of the source material. Steps to be followed 

1: Taking filename from user.
2: Break the corpus into individual words. To create a Markov model.
3: To display number of tokens and number of unique tokens.
4: Take an integer as user input and print the token with the corresponding index. 'EXIT' input must end the process. Make sure to handle all the error.

Before preceding enter the file name:'''

options = '''Here is the list of action you can perform in this application. Enter the number for which you want action to perform.

1- Total number of tokens.
2- Total number of unique tokens.
3- Token with the corresponding index. You have to enter the token index for the name.
4- Type "EXIT" to exit from the programme.

Enter the option:'''


def menu():
    file_name = input(starter)
    choice = input(options)
    while choice.lower() != 'exit':
        if choice.isdigit():
            if choice == '1':
                all_token = calculate_all_tokens(file_name)
                print(all_token)
            elif choice == '2':
                unique_token = calculate_unique_token(file_name)
                print(unique_token)

        choice = input(options)

menu()
