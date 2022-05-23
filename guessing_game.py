our_favourite_number = 17

user_number = input("Enter your favourite Number: ")

user_number = int(user_number)

if user_number == our_favourite_number:
    print("Wow!! You are absolutely right, our favourite number is" + " " + str(our_favourite_number))
elif user_number < our_favourite_number:
    print("Your number is lower, try again")
elif user_number > our_favourite_number:
    print("opps!! your number is higher, try a number lower")
else:
    print("Rest!!")