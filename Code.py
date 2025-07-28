# This project is based on Resturant menu bar 
menu = {'pasta':50,'chowmeen':20,'burger':30,'samosa':10,'cofee' : 40}
print("\n=============WELCOME SIR BHARAT RESTURANT==============\n")
print("Aap kya Order karna chate ho ")
print("\n1. Pasta : 50 Rs\n2. Chowmeen : 20 Rs\n3. Burger : 30 Rs\n4. Samosa : 10 Rs\n5. Cofee : 40 Rs")
total_amount = 0
order = input("Aapko kya order karna hai : ").lower()
quantity = int(input("Enter order quantity : "))
another_order = input("kya aap kuch or bhi order karna chate ho (yes/no) : ")
if order in menu:
    print("yes sir This order is avaliable wait only 5 minute")
    total_amount = total_amount+menu[order] * quantity
    if another_order == "yes":
        order_2 = input("sir or aap kya lena chate ho : ").lower()
        if order_2 in menu:
            print("okay sir ye order bhi hai humare Resturant main")
            total_amount = total_amount+menu[order_2] * quantity
            print(f"Sir This is your bill : {total_amount}")
    else:
        print(f"Sir This is your bill : {total_amount}")
else:
    print(f"Sorry sir {order} item is not available in this Resturant")
