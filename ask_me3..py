# In another file called ask_me_3.py, write code that does the following:
# a. Prompt the user for their name in a polite way
# b. Allow the user to enter their name
# c. Store the name in an appropriate variable name
# d. Greet the user using their name
# e. If the name is Jack or Jackie, greet the user using the respective name politely
# i. Say goodbye to the user and the program ends
# f. If the name is any other, greet the user by : ‘Hello Friend!!!’
# and do the following
# 1
# i. Prompt the user for their age
# ii. Allow the user to enter their age and store the age in an
# appropriate variable
# iii. If the age is less than 18, tell the user that they are
# below age of working
# iv. If the age is greater than 18 but less than 25, tell the
# user that they are of age to look for a job
# v. If the age is greater than or equal to 25 but less than 30,
# tell the user that they should be having a job already
# vi. If the age is greater than 30 but less than 60, tell the
# user that they should think about having a family.
# vii. If the age is less than 90 but greater than or equal to
# 60, tell the user that they should retire
# viii. If the age is not in any range we anticipated, say
# goodbye to the user with their name and show them the age they entered, tell them that they are alien in nature

name = input("What is your Name?")
if name == "Jackie" or name == "Jack":
    print("Goodbye " + name)
    exit
else:
    print("Hello Friend")
    age = input("What is your age?")
    if (int(age) < 18):
        print("You're are below age of working")
    elif (int(age) > 18 and (int(age) < 25)):
        print("You are of age to look for a job")
    elif (int(age) >=25 and (int(age) <30)):
        print("You should be having a job already")
    elif (int(age) > 30 and (int(age) < 60)):
        print("You should think about having a family")
    elif (int(age) >= 60 and (int(age) < 90)):
        print("You should think about having a family")
    else: 
        print("Goodbye" +" "+ name +" "+ "Youre" +age +"years Old of alient orign")