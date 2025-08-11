#By using classname 
#classnmae.propertyname
class Employee:
    eid=101
    ename='Rutuja'
    esalary=30000
obj1=Employee()
print(Employee.eid)
print(Employee.ename)
print(Employee.esalary)

#By using objectname 
#objectnmae.propertyname
class Employee:
    eid=101
    ename='Rutuja'
    esalary=30000
obj1=Employee()
print(obj1.eid)
print(obj1.ename)
print(obj1.esalary)
'''
This is a class 
have properties
eid=101
    ename='Rutuja'
    esalary=30000
'''
#to list down the properties of class and object we have to use
#print(Employee.__dict__)

#to create object properties
#SYNTAX: objectname.neewproerty=newValue
obj1.updatedSalary=40000

print(Employee.__doc__) #to get doc-string

help(Employee)  #taking help frompython related to the class

print(obj1.__doc__) #to get doc-string






class BankManage:
    account_name:'Rutuja Mane'
    account_no: 123456789
    withdraw_ammount= 3000
    deposit_ammount= 5000
    #current_ammount=deposit_ammount-deposit_ammount
newobj=BankManage()
print(BankManage.account_name)
print(BankManage.account_no)
print(BankManage)
print(BankManage)




