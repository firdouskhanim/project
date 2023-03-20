from admin import admin
from user import user 
import datetime as dt 
import sys
class main:
  def execute(self):
      while True:
            print("*"*80)
            print("WELCOME TO MY RESTAURANT".center(80),"\n")
            print("*"*80)
            print("[1.] ADMIN [2.] USER")
            choice=int(input("ENTER THE LOGIN FOR ADMIN AND USER"))
            if choice==1:
               obj=admin()
               t=dt.datetime.now()
               print("*"*40)
               print(t)
               print("*"*40)
               print("[1.] ADD FOOD ITEM \n[2.] LOGIN ID \n[3.] SEARCH MENU USING FOODID \n[4.] SHOW MENU \n[5.] REMOVE ITEM ")
               print("*"*80)
               select=int(input("ENTER YOUR CHOICE:    "))
              

               if select==1:
                  obj.add_item() 
                  
               if select==2:
                  show={}
                  selection=0
                  while selection !="n":
                        name=input("ENTER YOUR NAME:     ")
                        logid=int(input("ENTER THE login id:   "))
                        password=int(input("ENTER THE PASSWORD:    "))
                        show[logid]=[name,password]
                        selection=input("ENTER THE AGAIN NAME AND LOGIN ID [y/n]:    ")
                        obj.log_in(show)
                        
               if select==3:   
                  n=input("ENTER THE SEARCH FOOD ITEM ID:   ")
                  obj.view_item(n)

               if select==4:
                  print("SHOW THE MENU")
                  obj.display_food()
  
               if select==5:
                  food=int(input("ARE YOU WANT TO DELETE ITEM IN MENU:   "))
                  obj.remove_item(food)
                  print("SUCCESSFULLY DELETE IN MENU")

      


             
            if choice==2:
               obj1=user()
               t=dt.datetime.now()
               print(t)

               print("[1.] REGISTER APPLICATION FORM \n[2.] LOG IN APPLICATION \n[3.] USER DEFINE FACILITY \n[4.] UPDATE PROFILE")
               ch=int(input ("ENTER THE  USER CHOICE:  "))
               if ch==1:
                  print("THE USER CAN REGISTER IN APPLICATION")
                  obj1.show()

               if ch==2:
                  a=input(" ENTER THE NAME TO CONFIRM:  ")
                  b=input("INSERT PASSWORD TO CONFIRM:     ") 
                  obj1.log_in(a,b)  

               if ch==3:
                  option=int(input("[1.] SHOW ORDER \n[2.] PLACE NEW ORDER \n[3.] ORDER HISTORY  \nENTER YOUR CHOICE:     "))   
                  obj1.display(option)      

               if ch==4: 
                  k=input("ENTER THE USER ID :")
                  obj1.update_profile(k)
                  sys.exit()

if __name__=="__main__":
   obj2=main()
   obj2.execute()                  