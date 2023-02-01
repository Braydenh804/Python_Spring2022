# Prompt user for purchase amount, coupon amount, and percentage off the order
Price = float(input('Enter the amount of purchase : $'))
CashOff = float(input('Enter the cash coupon : '))
PercentOff = float(input('Enter the percent coupon : '))
# Define the TAX rate
TAX = 6
# Compute the total after cash coupon is applied
CashOffSubtotal = Price - CashOff
# Compute the total after percent coupon is applied
PercentOffSubtotal = CashOffSubtotal - ((PercentOff / 100) * CashOffSubtotal)
# Compute the total after TAX is applied
AfterTaxSubtotal: float = PercentOffSubtotal + ((TAX / 100) * PercentOffSubtotal)
# Now check in which shipping costs does the total qualify for
if AfterTaxSubtotal < 10:
    FinalTotal = AfterTaxSubtotal + 5.95
elif 10 <= AfterTaxSubtotal < 30:
    FinalTotal = AfterTaxSubtotal + 7.95
elif 30 <= AfterTaxSubtotal < 50:
    FinalTotal = AfterTaxSubtotal + 11.95
elif AfterTaxSubtotal >= 50:
    FinalTotal = AfterTaxSubtotal
# Display final cost
print('Total cost = $', round(FinalTotal, 2))
