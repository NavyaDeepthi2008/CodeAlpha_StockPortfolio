stock_prices={
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 320
}
total_investment=0

print("STOCK PORTFOLIO TRACKER")

while True:
    stock_name=input("Enter stock name or type DONE to finish: ").upper()
    if stock_name=="DONE":
        break
    if stock_name not in stock_prices:
        print("Stock not available.!!!")
        continue
    quantity=int(input("Enter Quantity: "))
    investment=stock_prices[stock_name]*quantity
    total_investment += investment

    print(f"Added {stock_name} investment: ${investment}")

print("\n💰 Total Investment Value: $", total_investment)
save=input("Do you want to save this into a file? (Yes/No): ").lower()
if save=="yes":
    file=open("Portfolio.txt","w")
    file.write(f"Total investment Value: ${total_investment}")
    file.close()
    print("Result saved in portfolio.txt")
    
