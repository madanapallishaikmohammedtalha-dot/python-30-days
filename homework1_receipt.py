#Homework 1 — The Receipt Calculator

apple_price=float(50)
banana_price=float(30)
milk_price=float(28)
apple=float(input("Apple(KG):"))
banana=float(input("Banana(dozens):"))
milk=float(input("Milk(liters):"))
apple_total = apple * apple_price
banana_total = banana * banana_price
milk_total = milk * milk_price
total = apple_total + banana_total + milk_total
print("\n======= RECEIPT =========")
print(f"Apples  {apple:.2f} kg x Rs {apple_price:.2f} = Rs {apple_total:.2f}")
print(f"Bananas {banana:.2f} dz x Rs {banana_price:.2f} = Rs {banana_total:.2f}")
print(f"Milk    {milk:.2f} L x Rs {milk_price:.2f} = Rs {milk_total:.2f}")
print("_____________________________")
print(f"Total:                  Rs {total:.2f}")
print("===========================")
