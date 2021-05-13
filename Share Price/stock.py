from bsedata.bse import BSE

b = BSE()

data = b.getScripCodes()
# print(data)

# value = b.getQuote("507685")
# # print(value)

# data1 = b.getQuote("532540")
# print(data1)

tg = b.topGainers()
# print(tg)

tl =b.topLosers()
# print(tl)


test = b.verifyScripCode("5325402")
print(test)