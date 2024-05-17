import random


system_guss = random.randrange(0,100)
while True:
    user_guss = int(input("enter a number"))
    if system_guss > user_guss:
        print("higher")
    elif system_guss < user_guss:
        print("lower")
    elif system_guss == user_guss:
        print("rght")
        break
