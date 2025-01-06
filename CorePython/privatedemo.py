# class BankAccount:
    
#     def __init__(self, account_number, acc_password):
#         self.account_number = account_number
#         self.acc_password = acc_password
       
# acc= BankAccount(123456, "password")  # Object creation       
# print(acc.account_number)
# print(acc.acc_password)       #not a good practice to give acess to password

#With Error: it will not allow to access the password outside the class
# class BankAccount:
    
#     def __init__(self, account_number, acc_password):
#         self.account_number = account_number
#         self.__acc_password = acc_password
       
# acc= BankAccount(123456, "password")  # Object creation       
# print(acc.account_number)
# print(acc.acc_password) 

class BankAccount:
    
    def __init__(self, account_number, acc_password):
        self.account_number = account_number
        self.__acc_password = acc_password
    def get_acc_password(self):
        print(self.__acc_password)       
       
acc= BankAccount(123456, "password")  # Object creation       
print(acc.account_number)
acc.get_acc_password()
# print(acc.acc_password) 