purchased = 2000
HePaid = 40.0
commission = .03 # 3 percent
HeSold = 42.75
sold = 200

amtPaid= purchased * HePaid
print("Joe paid", amtPaid, "dollars for his stocks")

purchCommission = amtPaid * commission
print("His broker was paid", purchCommission, "dollars during the purchase")

amountReceived = sold * HeSold
print("Joe's stocks sold for", amountReceived, "dollars")

sellCommission = amountReceived * commission
print("The broker was paid", sellCommission, "dollars during the sale")

amountLeft = amountReceived - sellCommission - purchCommission - amtPaid
if amountLeft < 0:
    print("Joe lost", abs(amountLeft), "dollars")
else:
    print("Joe made", amountLeft, "dollars")