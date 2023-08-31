# Defina uma classe BankAccount com atributos privados balance e account_number. 
# Crie métodos deposit e withdraw para manipular o saldo.

class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit (self, deposito): 
        self.balance = self.balance + deposito
        return self.balance
    def withdraw(self, sacar):
        self.balance = self.balance - sacar
        return self.balance
    
conta = BankAccount(100, 4321)
print(conta.deposit(50))

conta2 = BankAccount(100, 4321)
print(conta2.withdraw(50))

