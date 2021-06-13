from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyCodes

b = BtcConverter()
c = CurrencyCodes()

# print(b.get_latest_price("INR"))

#quantity,currency  (input)   --> output price 

quantity = float(input("Enter the quantity of Bitcoin you wanna Buy : "))
currency = input("Currency you wanna pay : ")
currency_symbol = c.get_symbol(currency)

bitcoin_symbol = b.get_symbol()

price = b.convert_btc_to_cur(quantity,currency)

print(f"{quantity}{bitcoin_symbol}  : {currency_symbol}{price}")

