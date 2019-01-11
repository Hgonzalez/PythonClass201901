import pandas as pd

stocks = ["TWTR", "GE", "GOOG"]
prices = [8.00, 2.00, 200.00]
info = list(zip(stocks,prices))
#print(info)

data = pd.DataFrame(data=info)
print(data)