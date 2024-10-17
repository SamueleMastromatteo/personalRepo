price_hour = 0.51
cost = input("you want the server for how much hour or day? ")
time = float(''.join(filter(str.isdigit, cost)))
if "hour" in cost:
    total_price = time * price_hour
elif "day" in cost:
    total_price = time * 24 * price_hour
else:
    total_price = 0
print(f"the total price is: {total_price} $")