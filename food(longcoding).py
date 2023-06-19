userdatabase={1:{'Username':'Yoga','Password':'123**','email':'yoga@gmail.com','phn_no':'9438798278'}}
class newuserr:
    def welcomeuser(self):#polymorphism
        print("Successfully signed in!!")
        print("Welcome user",self.userid)
    def signup(self):
        newuser={}
        self.userid=int(input("Userid:"))
        self.password=input("Password: ")
        self.username=input("Username")
        self.email=input("Email")
        self.phn_no=input('Phone no')
        newuser["Username"]=self.username
        newuser["Password"]=self.password 
        newuser["email"]=self.email
        newuser["phn_no"]=self.phn_no 
        userdatabase[self.userid]=newuser
        print(userdatabase)
        user2.welcomeuser()
class olduser(newuserr):#inheritance
    def login(self):
        self.userid=int(input("Userid:"))
        self.check()
    def check(self):
        if self.userid in userdatabase:
            self.c=userdatabase[self.userid]
            self.password=input("Password:")
            if(self.password==self.c["Password"]):
                user1.welcomeuser()
            else:
                print("Please enter valid login credentials")
                user1.login()
        else:
            user2.signup()
    def welcomeuser(self):
        print("Login succesful !!!\nWelcome user",self.c['Username'])
        fooditems=food()
        choice=int(input())
        if(choice==1):
            fooditems.vegres()
        else:
            fooditems.nonveg()
class food:
    global l1,l2,l3,f
    f=[]
    l1=[]
    l2=[]
    l3=[]
    def __init__(self,resid=None,resname=None,restype=None,ratings=None,available_food=None):
        self.resid=resid
        self.resname=resname
        self.restype=restype
        self.ratings=ratings
        self.available_food=available_food
    def vegres(self):
        res=[food(1,'A restaurant','Veg','* *',[[1,2,3],['Idli',"Dosa",'vada'],[20,30,40]]),food(2,'B restaurant','Veg','* * *',[[4,5,6],['Idli',"Dosa",'vada'],[20,30,40]])]
        for i in res:
            print(i.resid,'\n',i.resname,'\n',i.restype,'\n',i.ratings)
            f.append(i.resid)
            l1.append(i.available_food[0])
            l2.append(i.available_food[1])
            l3.append(i.available_food[2])
            for k in range(len(i.available_food)):
             for j in i.available_food:
                 print(j[k])
            
        o=order()
        o.placeorder()
    def nonveg(self):
        res=[food(1,'A restaurant','NonVeg','* *',[[1,2,3],['Chicken',"Mutton",'fish'],[20,30,40]]),food(2,'B restaurant','nonVeg','* * *',[[4,5,6],['Burger',"tandoori",'briyani'],[20,30,40]])]
        for i in res:
            print(i.resid,'\n',i.resname,'\n',i.restype,'\n',i.ratings)
            f.append(i.resid)
            l1.append(i.available_food[0])
            l2.append(i.available_food[1])
            l3.append(i.available_food[2])
            for k in range(len(i.available_food)):
             for j in i.available_food:
                 print(j[k])
            break
        o=order()
        o.placeorder()
class order:
    global cart
    global price
    cart=[]
    price=[]
    def __init__(self,orderid=None,orderfood=None,orderamount=None):
         self.orderid=orderid
         self.orderfood=orderfood
         self.orderamount=orderamount
    def placeorder(self):
      c=1
      while(c):
        a=int(input("enter the restaurantid :"))
        ind=f.index(a)
        self.orderid=l1[ind]
        self.orderfood=l2[ind]
        self.orderamount=l3[ind]
        n=int(input("enter the food id: "))
        if n in self.orderid:
            ind1=self.orderid.index(n)
            cart.append(self.orderfood[ind1])
            print(cart)
            price.append(self.orderamount[ind1])
        z=input("Place order y/n")
        if(z=='y'):
            c=0 
      print(cart)
      print(sum(price))
if __name__=='__main__':
    user1=olduser()
    #user2=newuserr()
    user1.login()
    #foodr=food()
    #foodr.vegres()
    
    
   
    
    
    
    
