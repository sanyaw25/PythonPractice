#BUILDING A ROBOT BARISTA
#Introduction
print(" Welcome to our cafe!")

name= input (" What is your name? \n ") 
if name == "Ben" or name == "Jake" or name == "ben" or name == "jake":
    evil_status= input(" Are you evil? \n ")
    good_deeds=int(input(" How many good deeds have you done today? \n "))
    if evil_status== "Yes" or "yes" and good_deeds < 3 :
        print( " You're not welcome here " + name +". Please leave. ")
        exit()
    else:
        print(" Oh, you're one of the nice ones. Sorry, come on right in. \n")
else: 
    print(" Hello " + name + ", thank you for coming in today. \n \n")
    
#Menu
Menu= "Black Coffee, Milk tea, Cappucino, Espresso, Chocolate Milkshake"
print(" " + name + ", Would you like to get something from our menu?")
answer = input(" Yes or no \n ")
if answer == "Yes" or answer== "yes":
    print("\n I'll be your server for today.")
elif answer == "No" or answer== "no":
    print(" Stop wasting our time! Get outta here!")
    exit()
else:
    print(" Sorry, I didn't understand")
    answer = input(" Yes or no \n ")
    if answer != "Yes" or "No" or "yes" or "no":  
        print("You're wasting our time. Get out!")
        exit()
    
print(" Here's what we're serving: \n "+ Menu)
order= input (" ")
quantity= int(input(" and how many servings would you like?\n "))

#Price List
if order=="Black Coffee" or "black coffee" or "coffee":
    price=6
elif order=="Milk Tea" or "milk tea" or "tea":
    price=5
elif order=="Cappucino" or "cappucino":
    price=8
elif order=="Espresso" or "espresso":
    price=7
elif order=="Chocolate Milkshake" or "chocolate milkshake" or "milkshake":
    price=10
else:
    print(" We don't have that here.")
total = price*quantity
print("\n "+ "Perfect, your total will be $" + str(total) + ". We'll be ready with your order of " + str(quantity)+" " + order + " shortly. ")

