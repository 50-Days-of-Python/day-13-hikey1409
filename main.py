#Write your code here.
price_of_an_item = int(input())
VAT =int(input())
try:
  c = price_of_an_item*VAT/100
except:
  print("invalid input")
else:
  d= c+price_of_an_item
finally:
  print(int(d))
