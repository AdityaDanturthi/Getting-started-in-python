import random

howmanydice = int(input("How many dice would you like to role?: "))
if (howmanydice == 0):
    print("Error: Please input the number of dice you would like to role agin! Should be greater than 0. ")
elif (howmanydice > 0):
    i = 0
    dicearr = []
    while i <howmanydice:
        dicenumber = random.randint(1,6)
        dicearr.append(dicenumber)
        i +=1


print(f"The number(s) are {dicearr}")