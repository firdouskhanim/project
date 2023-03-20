import json as js
import admin
class user:
  def __init__(self):
      self.detail={}
      self.food={}
  def show(self):
      customer=0
      while customer!="n":
            print("*"*80)
            userid=int(input("ENTER THE USERID :   "))
            name=input("ENTER THE FULL NAME:    ")
            mobno=input("ENTER THE MOBILE NUMBER:   ")
            email=input("ENTER THE EMAIL ID :   ")
            address=input("ENTER THE ADDRESS:    ")
            password=input("ENTER THE PASSWORD:    ")
            print("*"*80)
            self.detail[userid]=[ name,mobno,email, address,password] 
            customer=input("ENTER THE AGAIN USER DETAIL[y/n]:   ")
      f=open("user.json","w")
      js.dump(self.detail,f)
      f.close()
      

  def log_in(self,name,password):
      f=open("user.json")
      r=js.load(f)
      for i,j in r.items():
       if j[0]==name and j[4]==password:
           print("YOUR ARE LOG IN SUCCESSFULLY ")
           print("****WELCOME TO MY RESTAURANT****")
           f.close()    
       else:
           print("WRONG ID AND PASSWORD PLEASE TRY AGAIN.")   
    
  def display(self,option):
      self.option=option
      if option==1:
         print("***** SHOW ORDER*****")
         fh=open("data.json")
         r=js.load(fh)
         for i,j in r.items():
             print(i,j)
         
      if option==2:
         print("*****BOOK ORDER******")  
         fh=open("data.json")
         r=js.load(fh)
         order=input("ENTER THE FOOD ID :   ")
         for i,j in r.items():
           if i==order: 
              print(i,j)
              print("*"*80)
              j[0]=input("ENTER THE ADD FOOD ITEM:    ")
              j[1]=input("ENTER THE  ADD FOOD ITEM PRICE:  ")
              j[2]=int(input("ENTER THE FOOD  OF QUANTITY :  "))
              print("*"*80)
              self.food[i]=[j[0],j[1],j[2]]
         fh=open("order.json","w")
         js.dump(self.food,fh)
         fh.close()
         fh=open("order.json")
         r=js.load(fh)
         for i,j in r.items():
             print(i,j)
      if option==3:
         print("*****ORDER HISTORY*****")
         fh=open("order.json")
         r=js.load(fh)
         for i,j in r.items():
             print(i,j)     
  def update_profile(self,id):
      self.id=id
      f=open("user.json")
      r=js.load(f) 
      for i,j in r.items(): 
       if i==id:
          print("*"*80)
          j[0]=input("ENTER THE FULL NAME:    ")
          j[1]=input("ENTER THE MOBILE NUMBER:   ")
          j[2]=input("ENTER THE EMAIL ID :   ")
          j[3]=input("ENTER THE ADDRESS:    ")
          j[4]=input("ENTER THE PASSWORD:    ")
          print("*"*80)
          self.detail[i]=[j[0],j[1],j[2],j[3],j[4]]       
          f=open("user.json","w")
          js.dump(self.detail,f)
          f.close()
          f=open("user.json")
          r=js.load(f)
          for i,j in r.items():
              print(i,j)