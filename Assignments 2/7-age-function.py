def calculates(name,birthyear,weight):
    today = 2022
    age = today-birthyear
    print("your age is", age )

    name = name
    if name == "":
        name = "Lamara"
   
             
    print("you are", name,  "your weight is", weight, "age is",age)

weight = int(input("Enter your weight"))
name = str(input("what is your name?"))
calculates(name,2002,weight)