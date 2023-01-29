try:
    price= int(input())
    vat=int(intput())
    total= price+price*(vat)/100
    print(total)
except:
     print("Invalid")
