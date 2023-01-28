#Write your code here.
price_of_an_item = int(input())
VAT =int(input())
try:
  c = (price_of_an_item)*(VAT)/100
  d= c+price_of_an_item
  print(int(d))
except:
  print("Invalid Input")
