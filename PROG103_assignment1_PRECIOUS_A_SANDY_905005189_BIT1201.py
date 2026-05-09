#  Precious Vandi - Small Business Sales Calculator


sales_records = []
CURRENCY = "Le"   # Change to $, £, etc.


# Function to format money
def money(amount):
    return f"{CURRENCY}{amount:,.2f}"


# Function 1: Add Sale Record
def add_sale():
    while True:
        product = input("Enter Product Name: ")
        if product.replace(" ", "").isalpha():
            break
        print("Please enter letters only.")

    while True:
        try:
            quantity = int(input("Enter Quantity Sold: "))
            if quantity > 0:
                break
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            price = float(input("Enter Price per Unit: "))
            if price > 0:
                break
            print("Price must be greater than 0.")
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            cost = float(input("Enter Cost per Unit: "))
            if cost >= 0:
                break
            print("Cost cannot be negative.")
        except ValueError:
            print("Enter a valid number.")

    # Calculations
    revenue = quantity * price
    total_cost = quantity * cost
    profit = revenue - total_cost

    # Status
    if profit > 1000:
        status = "High Profit"
    elif profit > 0:
        status = "Moderate Profit"
    else:
        status = "Loss"

    record = {
        "product": product,
        "quantity": quantity,
        "price": price,
        "cost": cost,
        "revenue": revenue,
        "profit": profit,
        "status": status
    }

    sales_records.append(record)

    print("\n✅ Sale recorded successfully.")


# Function 2: View Sales Report
def view_sales():
    if not sales_records:
        print("No sales records available.")
        return

    print("\n========== SALES REPORT ==========")
    for i, r in enumerate(sales_records, start=1):
        print(f"\n--- Transaction {i} ---")
        print(f"Product        : {r['product']}")
        print(f"Quantity       : {r['quantity']}")
        print(f"Unit Price     : {money(r['price'])}")
        print(f"Revenue        : {money(r['revenue'])}")
        print(f"Profit         : {money(r['profit'])}")
        print(f"Status         : {r['status']}")
        print("---------------------------------")


# Function 3: Business Summary
def business_summary():
    if not sales_records:
        print("No data to summarize.")
        return

    total_revenue = sum(r["revenue"] for r in sales_records)
    total_profit = sum(r["profit"] for r in sales_records)

    print("\n========== BUSINESS SUMMARY ==========")
    print(f"Total Revenue : {money(total_revenue)}")
    print(f"Total Profit  : {money(total_profit)}")

    if total_profit > 0:
        print("Status        : PROFITABLE ✅")
    else:
        print("Status        : LOSS ❌")

    print("=====================================")


# Main Program
while True:
    print("\n=== Small Business Sales System ===")
    print("1. Add Sale")
    print("2. View Sales")
    print("3. Business Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_sale()

    elif choice == "2":
        view_sales()

    elif choice == "3":
        business_summary()

    elif choice == "4":
        print("Thank you for using this system.")
        break

    else:
        print("Invalid choice. Please select 1–4.")