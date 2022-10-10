    
    

score = input("Please enter score between 0.1 and 1: ")

if float(score) >= 0.9 and float(score)<=1:
    print("Your Grade is A.")
elif float(score) < 0.8 and float(score)<=1:
    print("Your Grade is B")
elif float(score) >= 0.7 and float(score)<=1:
    print("Your Grade is C")
elif float(score) >= 0.8 and float(score)<=1:
        print("Your Grade is D")
elif float(score) < 0.6 and float(score)<=1:
    print("Your Grade is F")
else: 
    print("Bad Score")

