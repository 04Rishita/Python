menu={
    "Pizza":150,
    "Pasta":100,
    "Fries":90,
    "Coffee":200,
    "Nachos":60
}
print("Welcome To My Cafe")
print("Pizza: Rs150\n Pasta: Rs100\n Fries: 90\n Coffee: 200\n Nachos: 60\n")
total=0
item1=input("enter item to order:")
if item1 in menu:
    total+=menu[item1]
    print(f"Your item {item1} is added")
else:
    print(f"Ordered item {item1} is not available")

another_order=input("Do you want another order item to add(yes/no):")
if another_order=="yes":
    item2=input("enter another item to order:")
    if item2 in menu:
        another_order=menu[item2]
        print(f"Item {item2} is added")
    else:
        print(f"Ordered item {item2} is not available")
print(f"The total amount for the orderd item is {total}")


