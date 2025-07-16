#rating app
rate=int(input("How much will you rate the app between 1-5?:")) #here user will rate in number
if 0<rate<=5:
    print("Thank you for your rating")

    if 0<rate<=3:
        print("what we need to improve?")
        feedback=input("Enter your feedback:")
        print("Thanks for the feedback!, we will work on it")
    elif 0<rate>3:
        print("We are glad to know you are enjoying the app!")
else:
    print("Invalid input, you are suppose to enter rating between 1-5")
