from ast import Try


user_no = input("Enter your number : ")

#Validation
try:
    user_no = int(user_no)
    if user_no >= 0:
        print("this is a positive number")

    else:
        print("this is not a positive number")

except:
    print("this is not a number")