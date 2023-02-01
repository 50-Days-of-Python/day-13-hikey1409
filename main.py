try:
    price= int(input())
    vat=int(input())
    total= price+price*(vat)/100
    print(round(total))
except:
    print("Invalid Input")
