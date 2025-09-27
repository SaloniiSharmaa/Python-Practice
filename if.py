# if = do some code only IF condition is True
# else do something else

age = int(input("Enter your age: "))

if age>=100:
    print("You are too old to signup!")

elif age>=18:
    print ("You are now signed up!")

elif age<0:
    print("You are not born yet.")

else: 
    print("You are not eligible to sign up.")
