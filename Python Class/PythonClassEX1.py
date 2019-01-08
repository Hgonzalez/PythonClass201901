# print("Hello World")
Bill_Amount = float(input("Please enter a number: "))
Tax_Rate = 0.08
Tip_Rate = 0.18

Total_Tax_Amount = (1 + Tax_Rate) * Bill_Amount
Total_Bill_Amount = (1 + Tip_Rate) * Total_Tax_Amount
print("Your Bill Will Be %s" %Total_Bill_Amount)