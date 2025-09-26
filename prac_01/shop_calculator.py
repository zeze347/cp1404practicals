Number_of_items = int(input("Number of items:"))
while Number_of_items <= 0:
	print("Invalid number of items!")
	Number_of_items = int(input("Number of items:"))
i = 1
total_price = 0
while i <= Number_of_items:
	Price_of_itesm = float(input("Price of items:"))
	total_price = total_price + Price_of_itesm
	i += 1
if total_price >= 100:
	total_price = total_price - total_price * 0.1
print(f"Total price of {Number_of_items} items is ${total_price:.2f}")
