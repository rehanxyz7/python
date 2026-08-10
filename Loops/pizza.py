print("----MENU----\n1.Add Toppings\n2.Exit")
choice= int(input("Enter the choice"))
while(choice!=2):
    print("What toppings to add: ")
    topping = input("Enter the topping:")
    print(f"The topping : {topping } is added succesfully to the pizza ")

    print("----MENU----\n1.Add Toppings\n2.Exit")
    choice= int(input("Enter the choice"))
    if(choice==2):
        print("EXIT\n")
        break