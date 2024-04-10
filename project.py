# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:06:41 2021

@author: Ramchandra Dalvi
"""

StartersItems=[
"1.French Fries Medium           ",
"2.Spring Roll (5)               ",
"3.Tangy Crispy Corn             ",
"4.Paneer Tikka + Green chutney  ",
"5.Gobi Manchurian with Ketchup  ",
"6.Garlic Bread 1 small          ",
"7.Nachos with Cheese Sauce      ", 
"8.Vegetable Cheese Balls        ",
"9.Pani Puri (6 Puri)            ",
"10.Tomato Soup with Crotons     "
]
StartersCost=[80,90,100,200,150,20,70,80,50,80]
MainItems=[
"1.Vegatable Biryani + Dry fruits",
"2.Pasta(White) + garlic bread(1)",
"3.Red Spagetti +  Sauted veggies",
"4.Palak Paneer +  Butter Naan(2)",
"5.Dal Makhani + Tandoori Roti(2)",
"6.Veg Burger loaded with  Cheese",
"7.Burritos with Soya,Tofu,Cheese",
"8.Curd Rice  served with  Pickle",
"9.Personal Size Margherita Pizza",
"10.Chole + Batoore( 2 ) +  Salad"
]
MainCost=[200,150,160,150,150,120,200,80,120,100]
DessertItems=[
"1.Brownie with Vanilla ice cream",
"2.Gajar Ka Halwa with dry fruits",
"3.Chocolate Ice cream  with Nuts",
"4.Vanilla IceCream + Choco sauce",
"5.Gulab Jamun 6 Large size Balls",
"6.Waffle with chocolate icecream"]
DessertCost=[150,100,80,80,90,140]

choice=4
Total=0
Start_Choose=0
Main_Choose=0
Dessert_Choose=0
Final_Items=[]
Final_Bill=[]
Final_quantities=[]
Final_Individual=[]
Order="Y"

print()
print()
print("Welcome to the Food Bliss \nWe hope you are having a great day!!")
print()
print()
print()

while Order=="Y":
   print("For the Starters Menu -------->Enter 1")
   print()
   print("For the Main Course Menu ----->Enter 2")
   print()
   print("For the Dessert Menu --------->Enter 3")
   print()
   print("To stop ordering ------------->Enter 4")
   print()
   choice=int(input("What is your choice ?"))


   while choice==1:
    print()
    print()
    print("Here is the Starters menu. Please choose the items you would like to order,one at a time.")
    choice1="Y"
    while choice1=="Y":
    
       for a in range (len(StartersItems)):
           print(StartersItems[a],"------>",StartersCost[a])# to print all the items in the list
           print()
       Start_Choose=int(input("Enter the item number"))
          
    
              
       q=int(input("Enter the quantity of the item selected"))
       
       if Start_Choose<=len(StartersItems):
        
         for b in range(len(StartersItems)):
           if b+1==Start_Choose:
              T_Start=StartersCost[b]*q
              Total+=T_Start
              print("Your current Total is",Total)
              Final_Items.append(StartersItems[Start_Choose-1])
              Final_quantities.append(q)
              Final_Bill.append(T_Start)
              Final_Individual.append(StartersCost[Start_Choose-1])
              print()
              
       else:
           print()
           print("ENTER A VALUE FROM THE LIST SHOWN!!")
             
       choice1=input("Do you wish to order more items from the same category? Type Y/N")

    print()        
    print("Your current Total is",Total)         
    print()
        
    choice=input("Enter Y to Load the Main Menu")
                     
                     
   while choice==2:
    print()
    print()
    print("Here is the Main Course menu. Please choose the items you would like to order,one at a time.")
    choice1="Y"
    while choice1=="Y":
    
    
       for a in range (len(MainItems)):
           print(MainItems[a],"------>",MainCost[a])# to print all the items in the list
           print()
       Main_Choose=int(input("Enter the item "))
       print()   
               
                    
       q=int(input("Enter the quantity of the item slected"))
       print()
       
       if Main_Choose<=len(MainItems):
        
         for b in range(len(MainItems)):
           if b+1==Main_Choose:
              T_Main=MainCost[b]*q
              Total+=T_Main
        
              print("Your current Total is",Total)
              Final_Items.append(MainItems[Main_Choose-1])
              Final_quantities.append(q)
              Final_Bill.append(T_Main)
              Final_Individual.append(MainCost[Main_Choose-1])
              print()
       else:
           print("ENTER A VALUE FROM THE LIST SHOWN!!")
             
       choice1=input("Do you wish to order more items from the same Category? Type Y/N")
            
    print("Your Current Total is",Total)         
    choice=input("Press Y to Load the Main Menu")     
   

   while choice==3:
    print()
    print()
    print("Here is the Dessert menu. Please choose the items you would like to order,one at a time.")
    choice1="Y"
    while choice1=="Y":
        
    
       for a in range (len(DessertItems)):
           print(DessertItems[a],"------>",DessertCost[a])# to print all the items in the list
           print()
       Dessert_Choose=int(input("Enter the item "))
          
     
              
       q=int(input("Enter the quantity of the item slected"))
       
       if Dessert_Choose<=len(DessertItems):
        
         for b in range(len(DessertItems)):
           if b+1==Dessert_Choose:
              T_Dessert=DessertCost[b]*q
              Total+=T_Dessert
              print("Your current Total is",Total)
              Final_Items.append(DessertItems[Dessert_Choose-1])
              Final_quantities.append(q)
              Final_Bill.append(T_Dessert)
              Final_Individual.append(DessertCost[Dessert_Choose-1])
              print()
       else:
           print("ENTER A VALUE FROM THE LIST SHOWN!!")
             
       choice1=input("Do you wish to order more items from the same Category? Type Y/N")

            
    print("Your current Total is",Total)         
    choice=input("Press Y to Load the Main Menu ")    
 
   if choice==4:
     break
print()
print()
print("Thank you for Dining with us.Your bill is as follows.We hope to see you soon!!!!!!") 
print()
print()
print("              Items             ","   Quantity ","    Price/serving    ","  Cost ")
print()
for k in range(len(Final_Items)): 
   print(Final_Items[k],"      ",Final_quantities[k],"              ",Final_Individual[k],'         ',Final_Bill[k])
   print()
print()
print()
print()


print("TOTAL BILL is",Total)
#