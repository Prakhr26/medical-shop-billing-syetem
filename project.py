# Medical Store Management System
# Simple Python script for a medical shop

# Sample inventory data
inventory = [
    {"name": "Paracetamol 650", "price": 15.0, "quantity": 50},
    {"name": "Dolo 650", "price": 30.0, "quantity": 8},
    {"name": "Combiflam", "price": 25.0, "quantity": 40},
    {"name": "Pantop 40", "price": 55.0, "quantity": 5}
]

def show_medicines():
    print("\n📋 Available Medicines")
    if not inventory:
        print("⚠️ No medicines in stock.")
        return
    
    print("Name                | Price (Rs.) | Quantity")
    print("-" * 45)
    for item in inventory:
        print(f"{item['name']:20} | {item['price']:10} | {item['quantity']:8}")

def add_medicine():
    print("\n➕ Add Medicine")
    name = input("Enter medicine name: ").strip()
    price = float(input("Enter price (Rs.): "))
    quantity = int(input("Enter quantity: "))

    for item in inventory:
        if item["name"].lower() == name.lower():
            item["quantity"] += quantity
            print(f"✅ Updated stock for {item['name']}.")
            return

    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"✅ Added new medicine: {name}")

def make_bill():
    print("\n🧾 Billing System")
    if not inventory:
        print("⚠️ No stock available.")
        return

    total = 0
    bill_list = []

    while True:
        med_name = input("Enter medicine name (or 'done' to finish): ").strip()
        if med_name.lower() == "done":
            break

        for item in inventory:
            if item["name"].lower() == med_name.lower():
                qty = int(input(f"Enter quantity for {item['name']}: "))
                if qty > item["quantity"]:
                    print(f"⚠️ Only {item['quantity']} left in stock.")
                else:
                    item["quantity"] -= qty
                    cost = qty * item["price"]
                    total += cost
                    bill_list.append({"name": item["name"], "qty": qty, "cost": cost})
                    print(f"✅ Added {qty} x {item['name']} to bill.")
                break
        else:
            print("❌ Medicine not found.")

    if bill_list:
        print("\n====== FINAL BILL ======")
        for b in bill_list:
            print(f"{b['name']} x {b['qty']} = Rs. {b['cost']}")
        print("------------------------")
        print(f"Total Amount: Rs. {total}")
        print("========================")

def check_low_stock():
    print("\n⚠️ Low Stock Alert")
    low_items = [item for item in inventory if item["quantity"] < 10]
    if low_items:
        for item in low_items:
            print(f"⚠️ {item['name']} - Only {item['quantity']} left!")
    else:
        print("✅ All items have enough stock.")

# Main Menu Loop
while True:
    print("\n=== MEDICAL STORE MENU ===")
    print("1. View Medicines")
    print("2. Add Medicine")
    print("3. Create Bill")
    print("4. Check Low Stock")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        show_medicines()
    elif choice == "2":
        add_medicine()
    elif choice == "3":
        make_bill()
    elif choice == "4":
        check_low_stock()
    elif choice == "5":
        print("👋 Thank you! Exiting program...")
        break
    else:
        print("❌ Invalid choice. Please try again.")
