# 1. accepts name input from keyboard and greet using the name stored in variable
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