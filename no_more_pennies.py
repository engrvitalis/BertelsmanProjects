"""
This programme will read prices from user until a blank line 
is entered. It will then display the total cost of all the 
entered items on one line, followed by the amount due if the 
customer pays with cash to the nearest nickel on the second 
line.

Input: Float
Output: String
"""
prices = []
while True:
    price = input("Please, enter item price: ")
    if price == "":
        break
    else:
        prices.append(float(price))

total_amount = sum(prices)

amount_in_cents = (total_amount * 100)
amount_in_nickel = amount_in_cents // 5

if amount_in_cents % 5 >= 2.5:
    amount_in_nickel += 1
    
# Total dollar amount to the nearest nickel
amount_due = amount_in_nickel / 20



print("")
print("Total amount: {:.2f}".format(total_amount))
print('Amount due for cash payment: {:.2f}'.format(amount_due))