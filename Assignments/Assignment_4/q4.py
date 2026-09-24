item_name = "Notebook"
unit_price = 10.00
quantity = 2
tax_rate = 0.05

subtotal = unit_price * quantity
tax_amount = subtotal * tax_rate
final_total = subtotal + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Final total: ${final_total:.2f}")
