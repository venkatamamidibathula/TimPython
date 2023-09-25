import datetime
import pytz
class Account:
    @staticmethod
    def _currenttime():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    def __init__(self,name,balance):
        self.name = name
        self.balance= balance
        self.tranactlog = [(Account._currenttime(),balance)]
        print("Account created for "+ self.name)
        self.showbalance()
    def deposit(self,amount):
        self.balance += amount
        self.tranactlog.append((Account._currenttime(), amount))
        self.showbalance()
    def withdraw(self,amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            self.tranactlog.append((Account._currenttime(),-amount))
        else:
            print("Insufficient funds")
        self.showbalance()
    def showbalance(self):
        print(f"Balance left is {self.balance}")
    def displaytrans(self):
        for date, amount in self.tranactlog:
            if amount > 0:
                transc_type = 'deposited'
            else:
                amount*=-1
                transc_type='withdrawn'
            print("{:6} {} on {} local time was {}".format(amount,transc_type,date,date.astimezone()))

if __name__ == '__main__':
    tim = Account("Tim",800)
    tim.deposit(1000)
    tim.deposit(500)
    tim.withdraw(8000)
    tim.displaytrans()