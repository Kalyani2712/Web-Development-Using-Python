code = int(input("Enter product code (1, 2, or 3): "))
order_amount = float(input("Enter order amount: "))

if code == 1 and order_amount > 1000:
    discount = 0.10 * order_amount
elif code == 2 and order_amount > 100:
    discount = 0.05 * order_amount
elif code == 3 and order_amount > 500:
    discount = 0.10 * order_amount
else:
    discount = 0

net_amount = order_amount - discount
print(f"The net amount to be paid is {net_amount:.2f}")
