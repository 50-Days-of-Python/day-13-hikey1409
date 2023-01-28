def calculate_price_with_vat(price_of_an_item,VAT):
    try:
        vat = float(price_of_an_item) * float(VAT) / 100
        total_price = float(price_of_an_item) + vat
        return total_price
    except:
        return "Invalid input"

price_of_an_item = input()
VAT = input()

total_price = calculate_price_with_vat(price_of_an_item,VAT)
print(round(total_price))
