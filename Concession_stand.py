#Author : CyberKAT
#Starbucks Concession stand
name= input('Hello, what is your name\n')
Total = 0

print(f"Hello, {name} ,What would you like to order")
print("")
print('Here is our menu ')

Menu = {
    'black coffee':40, 
    'latte':50, 
    'white coffe':35, 
    'cappucino':40}
 
while True:
    print('---------MENU-------')
    for item,price in Menu.items():
       print(f"{item}: R{price}")
    
    Order = input('\nEnter your order (q to Quit): ').strip().title().lower()
    if Order == "q":
        break 
    if Order in Menu:
        Total += Menu[Order]
        print(f'{Order} added! Current total: {Total}')
    else :
        print("That item is not on the menu.")

print(f'\nFinal Total: R{Total}')


