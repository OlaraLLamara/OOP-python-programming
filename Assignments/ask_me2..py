#In another file called ask_me_2.py, modify ask_me.py to do the following:
#a. Write code executing tasks a,b,c,d from question 1
#b. If the user does not enter a name, say: Hello Stranger

name = input("What is your Name?")
if name:
    print("Greetings " + name)
else:
    print("Greetings Stranger")
    