from forex_python.converter import CurrencyRates

c1 = CurrencyRates()

amount = float(input("Enter the amount : ")) # 1

from_currency = input("Enter your Currency : ").upper() # USD 
to_currency = input("to which Currency : ").upper()  #INR

converter = c1.convert(from_currency,to_currency,amount)

converter = str(round(converter,2))

print(f" {from_currency } to {to_currency} : {converter}")


# print(c1.get_rates("INR"))

# print(c1.get_rate("USD","INR"))
