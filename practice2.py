import random

print("this is a computer number guessing game ")

first = input("do you wanna play the game ? ")
if first.lower() != "yes":
    quit()
else :
    print("lets go. vamos!!")

second = input("plz enter a number greater than zero ")

if second.isdigit():
    second = int(second)

    if second <= 0:
        print("please enter a number greater than zero")
        quit()

else:
    print("please enter a number next time")
    quit()

third = random.randint(0,second)
rath = 0
while True:
    rath += 1
    fourth = input("make a guess : ")

    if fourth.isdigit():
        fourth = int(fourth)
    else :
        print("enter a number next time")
        continue
    if fourth == third :
        print("habibi you got it")
        break
    elif fourth > third:
        print("your guees is bit high")
    else  :
        print("your guees is bit low ")
        
print("your score is: ", rath)


