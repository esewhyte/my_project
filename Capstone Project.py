#start by importing the random module
import random
import string

number_of_digits = 3
number_of_punctuation_characters = 2
password_length = 15
characters = string.ascii_letters + string.digits + string.punctuation

# create an empty string called password
password = ""   

#use the function random.choice() which returns a random character from a sequence.
for digits_index in range(number_of_digits):
        password = password + random.choice(string.digits)
        
 #the + symbol is used to concatenate the three sets of characters to create a single string 
 # that we will assign to the characters variable.
        
for punctuation_index in range(number_of_punctuation_characters):
        password = password + random.choice(string.punctuation)
for index in range(password_length):
    password = password + random.choice(characters)
    
#To shuffle characters in the password string we will use the random.shuffle() function.   
def randomize_password(password):
    password_list = list(password)
    random.shuffle(password_list)
    return "".join(password_list)

#This function converts the password string into a list before applying random.shuffle.
# Then it returns a string using the string join method.


print("Password generated: {}".format(randomize_password(password)))


