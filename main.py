import time

cat_attributes = {
    "intelligence": 15,
    "energy": 50,
    "weight": 30,
}

print("Welcome to my cat game!")

name = input("Enter name: ")
colour=input("Enter a colour: ")

while True:

    print("What would you like to do? 1. Play with your cat 2. Train your cat 3. Show stats 4. Feed your cat 5. Put your cat to sleep ")
    option = input()

    if option == '1':
        if cat_attributes["energy"] < 5:
            print(name + " is too tired to play right now!")
        else:
            cat_attributes["energy"]=(cat_attributes["energy"])-5
            cat_attributes["weight"] = (cat_attributes["weight"])-5
            cat_attributes["intelligence"] = (cat_attributes["intelligence"])-1
            print("-5 Energy -5 Weight -1 Intelligence")

    elif option == '2':
        if cat_attributes["weight"] < 5:
            print(name + " is too hungry to learn right now!")
        else:
            cat_attributes["intelligence"]=(cat_attributes["intelligence"])+5
            cat_attributes["energy"]=(cat_attributes["energy"])-5
            print("+5 Intelligence -5 Energy")

    elif option == "3":
        for item in cat_attributes:
            print(item + ": " + str(cat_attributes[item]))

    elif option == "4":
        if cat_attributes["intelligence"] < 10:
            print("Uh oh... It seems your cat has forgotten how to eat!")
            print("Intelligence: " + str(cat_attributes["intelligence"]))
        
        else:
            cat_attributes["energy"] = (cat_attributes["energy"])+5
            cat_attributes["weight"] = (cat_attributes["weight"])+10
            print("+5 Energy +10 Weight")
    
    elif option == "5":
        cat_attributes["energy"] = (cat_attributes["energy"])+10
        print("+10 Energy")
        
    else:
        pass

    if cat_attributes['energy'] < 0:
        
        print("Your cat has collapsed!")
        print("Energy: " +str(cat_attributes["energy"]))

        for i in range (5):
            print(".")
            time.sleep(1)

        print("Your cat has woken up.")

        cat_attributes["energy"]=cat_attributes["energy"]+10
        cat_attributes["weight"]=cat_attributes["weight"]-10

        print("+10 Energy -10 Weight")

    elif cat_attributes["weight"] < 0:

        print("Weight:" + str(cat_attributes["weight"]))
        print("You've not fed your cat for too long!")
        print(name + " has died.")
        break

    elif cat_attributes["intelligence"] < 0:

        print("Uh oh! It looks like your cat has forgotten how to breathe!")
        print("Intelligence: " + str(cat_attributes["intelligence"]))
        print(name + " has died.")
        break