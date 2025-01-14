distance = float(input("Enter distance in kilometers: "))

if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = distance * 10
else:
    fare = distance * 12

print(f"The fare for {distance} km is Rs. {fare:.2f}")

