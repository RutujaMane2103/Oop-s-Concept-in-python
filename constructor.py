''''
class company:
    company_name='WIPRO'
    location='PUNE'
    def __init__(self,empid,name,salary):
        self.empid=empid     #self.PropertyName=argument_value
        self.name=name
        self.salary=salary
        print(f"Employee details added ! !")

    def propPrinter(self):
        print(f"Empid:{self.empid} | Name:{self.empid} | Salary:{self.salary} ")

obj=company(101,'Raj',50000)
obj2=company(102,'Priya',30000)
obj3=company(103,'Akshay',70000)

obj.propPrinter()
obj2.propPrinter()
obj3.propPrinter()
'''
##############################################################################################

##########_________TASK____________##############

class Bank:
     Bank_name='IFCS'
     IFSC= 123456
     Location= 'Kalamboli'
     def __init__(self,Acc_no,Name,Balance,Loans):
          self.Acc_no=Acc_no
          self.Name=Name
          self.Balance=Balance
          self.Loans=Loans
          print(f"___________Deatils of customer's successfully added____________ ")
          
     def get_details(self):
          print(f"Bank name: {self.Bank_name}")
          print(f"IFSC: {self.IFSC}")
          print(f"Location: {self.Location}")
          print(f"Acc_no: {self.Acc_no}")
          print(f"Name: {self.Name}")
          print(f"Balance: {self.Balance}")
          if len(self.Loans)==0:
              print(f"Loans: No loan")
          else:
               print(f"Loans:{self.Loans} ")
          print("----------------------------------------------------------------")

     
     def get_loan(self,loan_amount):
          res=self.Balance*3
          if loan_amount<=res and len(self.Loans)<3:
               print(f"Loan amount :{loan_amount}")
               print(f"Your loan amount is applicable | You are eligible for loan.")
               
          else:
               print(f"You are not eligible for loan.")
               print(f"Try to get rid of one of the previous loan.")
          print("----------------------------------------------------------------")

     def deposit(self,amount):
          if amount>0:
               self.amount=amount
               self.Balance+=amount
               print(f"Deposit amount:{amount}")
               print(f"Update balance:{self.Balance}")
               print(f"Deposit successful ! !")
          else:
               print("Plz...Enter the valid amount to deposit")
          print("----------------------------------------------------------------")


     def withdraw(self,withdraw_amount):
          if withdraw_amount<=self.Balance:
               self.Balance-=withdraw_amount
               print(f"Withdraw amount:{withdraw_amount}")
               print(f"Updated balance :{self.Balance}")
               print(f"Withdraw successfully ! !")
          else:
               print(f"Withdraw amount is insufficient!!!")

obj=Bank(123456789876,'Rutuja Mane',10000,['Car loan','Home loan'])   
obj.get_details()    
obj.get_loan(30000) 
obj.deposit(5000)
obj.withdraw(15000)
    

###################################################################################

