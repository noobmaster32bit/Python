selling_price=int(input("enter the selling price:"))
cost_price=int(input("enter the cost price:"))

profit=selling_price-cost_price
print(f"profit is ={profit}")

profit_percentage=(profit/cost_price)*100
print(f"profit percentage is ={profit_percentage}")
