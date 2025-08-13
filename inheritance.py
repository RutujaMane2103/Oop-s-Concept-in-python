'''
class parent:
    a=10
    b=20
    def printer(self):
        print('Inside the parent class')

#Inheritance the parent class   
class child(parent):
    c='Hello'  #creating the properties of child class
    def cprinter(self):
        print('Inside child class')

#creating object of child class
obj=child()
print(obj.a)     #accessing properties of parent class using child class object
print(obj.b)
obj.printer()

print(obj.c)
obj.cprinter()


######################## When we use constructor in inheritance ###############################
class parent:
    def __init__(self,pare):
        self.parent=pare
    def printer(self):
        print(f"Inside parent class : {self.parent}")

class child(parent):
    def __init__(self,paree,childd):
        parent.__init__(self,paree)
        self.childd=childd
    def cprinter(self):
        print(f"Inside child class child : {self.childd}")

obj=child(101,102)
obj.printer()
obj.cprinter()

'''
#######################################INSTAGRAM TASK ON INHERITANCE ###############################################
class instagram1:
    username='Rutuja'
    password=123456

    def __init__(self,bio):
        self.bio=bio
    
    def get_details(self):
        print(f"Username :{self.username} |Passoword :{self.password}")
        print(f"Username :{self.username}")
        print(f"Bio : {self.bio}")

class instagram2(instagram1):
    def __init__(self, reels):
        instagram1.__init__(self,reels)
        self.reels=reels
    
    def get_details2(self):
        print(f"Reels posted by {self.username} related to {self.reels}")

    def chats(self,chat):
        self.chat=chat
        print(f"Chats with {self.username}")
    
    def posts(self,post):
        self.post=post
        print(f"Post added :{self.post}")

obj=instagram2('Python Fullstack Developer')
obj.get_details()
obj.chats("New chat")
obj.posts("Constructor,Decorator")
obj.get_details2()

