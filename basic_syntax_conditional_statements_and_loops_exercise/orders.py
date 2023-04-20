number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_need_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_need_per_day < 1 or capsule_need_per_day > 2000:
        continue
    total = price_per_capsule * days * capsule_need_per_day
    total_price += total
    print(f"The price for the coffee is: ${total:.2f}")
print(f"Total: ${total_price:.2f}")
