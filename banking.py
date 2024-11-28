class BankAccount:
  def __init__(self, user_name, balance):
    self.user_name = user_name
    self.balance = balance
  
  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      return f"Deposit {amount} TK successfully"
    else:
      return f"Invalid Amount"
  
  def getBalance(self):
    return self.balance
  
  def withdraw(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      return f"Withdraw {amount} TK successfully"
    else:
      return f"Insufficient Balance"
    
object = BankAccount('Amin Babu', 10500)

print(f"Account name is {object.user_name}")
print(f"Initial Balance is {object.balance}")
print(object.deposit(2000))
print(f"After Deposit, Your Balance is {object.getBalance()}")
print(object.withdraw(2500))
print(f"After withdraw, Your Balance is {object.getBalance()}")