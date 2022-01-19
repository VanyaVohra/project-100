class ATM(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    def BalanceEnquiry(self):
        print("Your balance is 100rs")
    
    def CashWithdrawl(self):
        print("How much do you want to withdraw?")

vanya = ATM(123456, 1234)
print(vanya.BalanceEnquiry)