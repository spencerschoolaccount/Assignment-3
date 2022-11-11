pizzaSize = input('Would you like a large or an extra large pizza? \n')

if pizzaSize.lower() == 'large':
  pizzaCost = 6.00
elif pizzaSize.lower() == 'extra large':
  pizzaCost = 10.00
else:
  exit('Invalid input, please restart program')

toppingAmount = input('How many toppings would you like? (1, 2, 3, or 4 \n')

if toppingAmount == '1':
  toppingCost = 1.00
elif toppingAmount == '2':
  toppingCost = 1.75
elif toppingAmount == '3':
  toppingCost = 2.50
elif toppingAmount == '4':
  toppingCost = 3.35
else:
  exit('Invalid input, please restart program')

Subtotal = pizzaCost + toppingCost
print("""Your receipt is:
Subtotal: $""" + str(Subtotal) + """
Tax: $""" + str(round(Subtotal*0.13,2)) + """
Total: $""" + str(round(Subtotal*1.13,2))
)