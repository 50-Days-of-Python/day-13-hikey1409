price_of_an_item = float(input())
VAT =float(input())
try:
  c = (price_of_an_item)*(VAT)/100
  d= c+price_of_an_item
  print(round(d))
except:
  print("Invalid Input")
