
foods = [] # empty LIST of food, they need to be selected 
Prices = [] # empty LIST of prices
total = 0 # The price before picking food

# Use the while loop with a boolean
while True:
    food = input('Enter a food in cart(q to quit): ')
    if food.lower() == "q": 
        break 
    else:
        Price = float(input(f'Enter the price of a {food}: R'))
        foods.append(food) # adds food picked to the foods LIST
        Prices.append(Price) # adds the entered price to prices list


print('---- Your cart----')# Escape the loop with q and the cart will be shown

for food in foods: # This will list the foods
    print(food, end= ' ')

for Price in Prices: #This will calculate the price
    total += Price 
print('')
print(f'Your total is: R{total}')