# hat_list = [1, 2, 3, 4, 5]
# user_input = int(input("entere a number to replace the middle number"))

# hat_list[len(hat_list)/2] = user_input;
# print(hat_list)



hat_list = [1, 2, 3, 4, 5]


user_input_number = int(input("enter a number to replace the middle number in the array above"))


hat_list[len(hat_list) // 2] = user_input_number #used to calculate the midle number and to asign user input to it
print("the new list with middle number replaced is:", hat_list)

hat_list.pop(-1) #used to remove last element in list

print("the list with the last number popped off is ", hat_list)

print("the length  of the ramainiing array is:",len(hat_list))