price_of_an_item = input()
VAT = input()
try:
  c = float(price_of_an_item)*float(VAT)/100
  d= c+price_of_an_item
  print(round(d))
except:
  print("Invalid Input")
