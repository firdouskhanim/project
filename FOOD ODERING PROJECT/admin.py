import json as js
from user import user 
class admin:
  def __init__(self):
      self.data={}
      self.login={}
     
  def add_item(self):
      choose=0
      while choose!="n": 
            print("*"*70)
            print("MENU".center(70),"\n")
            print("*"*70)
            foodid=int(input("ENTER THE FOOD ID :"))
            item=input("ENTER THE ADD FOOD ITEM:    ")
            price=input("ENTER THE  ADD FOOD ITEM PRICE:  ")
            self.qty=int(input("ENTER THE FOOD  OF QUANTITY:  "))
            discount=int(input("ENTER THE DISCOUNT:   "))
            print("*"*70)
            self.data[foodid]=[item,price,self.qty,discount]
            choose=input("ARE YOU WANT TO AGAIN ADD FOOD ITEM [y/n]:    ")
      fh=open("data.json","w")
      js.dump(self.data,fh)
      fh.close()
      
       

  def log_in(self,login):
      self.login=login
      print("*"*80)
      name=input("ENTER THE NAME:   ")
      id=input("ENTER THE LOG ID:  ")
      print("*"*80)
      fh=open("login.json","w")
      js.dump(self.login,fh)
      fh.close()
      fh=open("login.json")
      r=js.load(fh)
      for i,j in r.items():
       if i==id and j[0]==name:
          print(f"ADMIN LOGIN ID {i} NAME {j[0]} PASSWORD {j[1]} ") 
          print("YOUR LOGIN  SUCCESSFULLY")
          fh.close()
       else: 
          print("WRONG ID , PLEASE TRY AGAIN  ")

  def view_item(self,itemid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
        if itemid==i:
           print(i,j)
         
  def display_food(self):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
          print(i,j)

  def remove_item(self,itemid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
        if i==itemid:
           del(r[i])
      fh.close()   
      fh=open("data.json","w")
      js.dump(r,fh)
      fh.close()

 