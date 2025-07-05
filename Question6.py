# Item prices and quantities
item_prices = [10.0, 5.0, 2.5]
quantities = [2, 4, 3]

# Discount and tax rates (in percentages)
discount_rate = 10  # 10%
tax_rate = 8        # 8%

# Calculate subtotal for each item
subtotals = [p * q for p, q in zip(item_prices, quantities)]

# Total before discount
total_before_discount = sum(subtotals)

# Apply discount
discount_amount = total_before_discount * (discount_rate / 100)
total_after_discount = total_before_discount - discount_amount

# Apply tax
tax_amount = total_after_discount * (tax_rate / 100)
final_total = total_after_discount + tax_amount

# Output the final total
print(f"Final Total: ${final_total:.2f}")
