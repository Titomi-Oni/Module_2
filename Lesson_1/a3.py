# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car
print ("Select your ride")
print ("1 for bike")
print ("2 for car")
# 2) Take the user’s input and store it in `choice`.
choice = int(input("Enter your choice:"))
# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"
if choice==1:
    print("What type of bike")
    print("1 for Scooter")
    print("2 for scooty")
    choice2 = int(input("Enter your bike choice:"))
    if choice2==1:
        print("You have selected Scooter")
    else:
        print ("You have selected Scooty")
# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"
elif choice ==2:
    print ("What type of car")
    print ("1 for Sedan")
    print ("2 FOR XUV")
    choice3 = int(input("Enter your car choice:"))
    if choice3==1:
        print("You have selected Sedan")
    else:
        print ("You have selected XUV")
# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"
else:
    print ("Wrong choice")