num_items = int(input("Enter number of items: "))
subtotal = 0
tax_8 = 0
tax_10 = 0
for i in range(num_items):
    print(f"\nItem {i + 1}")
    name = input("Enter item name: ")
    price = int(input("Enter item price (yen): "))
    item_type = input("Enter type (food/other): ").strip().lower()
    while item_type not in ("food", "other"):
        print("Invalid type. Please enter food or other.")
        item_type = input("Enter type (food/other): ").strip().lower()
    if item_type == "food":
        tax = price * 8 // 100
        tax_8 += tax
    else:
        tax = price * 10 // 100
        tax_10 += tax
    subtotal += price
    print(f"{name} ¥{price} (tax ¥{tax})")
total_before_discount = subtotal + tax_8 + tax_10
if total_before_discount >= 1000:
    discount = 50
else:
    discount = 0
final_total = total_before_discount - discount
print("\n========== RECEIPT ==========")
print(f"Subtotal: ¥{subtotal}")
print(f"8% tax: ¥{tax_8}")
print(f"10% tax: ¥{tax_10}")
print(f"Total before discount: ¥{total_before_discount}")
print(f"Discount: ¥{discount}")
print(f"Total: ¥{final_total}")
print("=============================")