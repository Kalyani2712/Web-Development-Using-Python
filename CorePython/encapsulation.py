#create a class BankAccount now create a constructor that take Balance(private) as input and deposit fuction to add or substract money from the Bank Account.
class BankAccount:
    def __init__(self, balance=0):
        """
        Constructor to initialize the balance (private attribute).
        :param balance: Initial balance in the bank account (default is 0).
        """
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """
        Function to add money to the account.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Function to subtract money from the account.
        :param amount: Amount to withdraw.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        """
        Function to get the current balance.
        :return: The current balance.
        """
        return self.__balance


# Example usage
account = BankAccount(1000)  # Initializing with a balance of 1000
account.deposit(500) 
account.deposit(1500)  
account.deposit(200)         
account.withdraw(300) 
account.withdraw(1000)    
account.withdraw(2000)  
print("Current Balance:", account.get_balance())  # Display current balance
