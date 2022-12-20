import time

products = """
Products:
Beverages------------------------------------------
Code:                        
   A1 - Bottle of Water = 1AED       
   B1 - Can of Pepsi = 3AED        
   C1 - Can of Sprite = 3AED       
   D1 - Can of Coke = 3AED         
   E1 - Iced Coffee = 8AED           
   F1 - Iced tea = 4AED            

Snacks-----------------------------------------------
   A2 - Small Doritos = 4AED         
   B2 - Small Lays chips = 4AED    
   C2 - Croissant = 3AED             
   D2 - Muffin = 5AED                
   E2 - Turkey Ham sandwich = 10AED  
   F2 - Tuna Sandwich = 10AED        
"""

print(products) #Prints the Vending Machine's menu


#Price
water = float(1)
pepsi = float(3)
sprite = float(3)
coke = float(3)
coffee = float(3)
tea = float(4)

doritos = float(4)
lays = float(4)
croissant = float(3)
muffin = float(5)
turkey = float(10)
tuna = float(10)


time.sleep(1)
#Variables set for the products' prices
que = False
while que == False:
    money_in = float(input("Insert cash: "))
    print("\nAmount of money received:", money_in)
    prdct_code = input("Enter product code: ")
    #Prints the message to enter cash and input code and which runs the selected code's function




    #Bevs
    def A1():
         if money_in >= water: #When the amount of money inputed is greater than the price of product, it will proceed with the program, else it tells the user how much more money is needed
            sug = input("""We recommend chips with this product, Would you like to purchase?
00. Doritos
01. Lays
02. None
Input: """)
            sukli = 0
            if sug == "00":
                doriwater = doritos + water
                if money_in > doriwater:
                    print('Dispensing a Bag of Doritos and a Bottle of Water')
                    sukli = money_in - doriwater
                    print(sukli)
                elif doriwater > money_in: #Goes here if user didnt put enough money in, and asks for more money
                    remain = doriwater - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "01":
                layswater = lays + water
                if money_in > layswater:
                    print('Dispensing a Bag of Lays and a Bottle of water')
                    sukli = money_in - layswater
                    print(sukli)
                elif layswater > money_in: 
                    remain = layswater - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "02":
                change = money_in - water
                print("\nDispensing Bottle of Water")
                print("Your change is" , change)  
               #Recommends user certain products with this product
         else:
            remain = water - money_in
            print("Cash insufficient. Amount pending:", remain) #Shows how much money is pending


    def B1():
         if money_in >= pepsi:
            change = money_in - pepsi
            sug = input("""We recommend chips with this product, Would you like to purchase?
00. Doritos
01. Lays
02. None
Input: """)
            sukli = 0
            if sug == "00":
                doripepsi = doritos + pepsi
                if money_in > doripepsi:
                    print('Dispensing a Bag of Doritos and a Can of Pepsi')
                    sukli = money_in - pepsi
                    print(sukli)
                elif doripepsi > money_in:
                    remain = doripepsi - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "01":
                layspepsi = lays + pepsi
                if money_in > layspepsi:
                    print('Dispensing a Bag of Lays and a Can of Pepsi')
                    sukli = money_in - layspepsi
                    print(sukli)
                elif lays > money_in:
                    remain = layspepsi - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "02":
                change = money_in - pepsi
                print("\nDispensing Can of Pepsi")
                print("Your change is" , change)  
         else:
            remain = pepsi - money_in
            print("Cash insufficient. Amount pending:", remain)
        
            
    def C1():
         if money_in >= sprite:
            change = money_in - sprite
            sug = input("""We recommend chips with this product, Would you like to purchase?
00. Doritos
01. Lays
02. None
Input: """)
            sukli = 0
            if sug == "00":
                dorisprite = doritos + sprite
                if money_in > dorisprite:
                    print('Dispensing a Bag of Doritos and a Can of Sprite')
                    sukli = money_in - dorisprite
                    print(sukli)
                elif dorisprite > money_in:
                    remain =  dorisprite - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "01":
                layssprite = lays + sprite
                if money_in > layssprite:
                    print('Dispensing a Bag of Lays and a Can of Sprite')
                    sukli = money_in - layssprite
                    print(sukli)
                elif layssprite > money_in:
                    remain = layssprite - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "02":
                change = money_in - sprite
                print("\nDispensing Can of Sprite")
                print("Your change is" , change)
         else:
            remain = sprite - money_in
            print("Cash insufficient. Amount pending:", remain)
        
    def D1():
         if money_in >= coke:
            change = money_in - coke
            sug = input("""We recommend chips with this product, Would you like to purchase?
00. Doritos
01. Lays
02. None
Input: """)
            sukli = 0
            if sug == "00":
                doricoke = doritos + coke
                if money_in > doricoke:
                    print('Dispensing a Bag of Doritos and a Can of Coke')
                    sukli = money_in - doricoke
                    print(sukli)
                elif doricoke > money_in:
                    remain =  doricoke - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "01":
                layscoke = lays + coke
                if money_in > layscoke:
                    print('Dispensing a Bag of Lays and a Can of Coke')
                    sukli = money_in - layscoke
                    print(sukli)
                elif layscoke > money_in:
                    remain = layscoke - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "02":
                change = money_in - coke         
                print("\nDispensing Can of Coke")
                print("Your change is" , change)
         else:
            remain = sprite - money_in
            print("Cash insufficient. Amount pending:", remain)
        
    def E1():
         if money_in >= coffee:
            change = money_in - coffee
            sug = input("""We recommend these Food items with this product, Would you like to purchase?
00. Muffin
01. Croissant
02. None
Input: """)
            sukli = 0
            if sug == "00":
                muffcoffee = muffin + coffee
                if money_in > muffcoffee:
                    print('Dispensing a Muffin and a Can of Coffee')
                    sukli = money_in - muffcoffee
                    print(sukli)
                elif muffcoffee > money_in:
                    remain =  muffcoffee - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            elif sug == "01":
                croscoffee = croissant + coffee
                if money_in > croscoffee:
                    print('Dispensing a Croissant and a Can of Coffee')
                    sukli = money_in - croscoffee
                    print(sukli)
                elif croscoffee > money_in:
                    remain = croscoffee - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "02":
                change = money_in - coke                    
                print("\nDispensing Can of Coffee")
                print("Your change is" , change)
         else:
            remain = coffee - money_in
            print("Cash insufficient. Amount pending:", remain)

    def F1():
         if money_in >= tea:
            change = money_in - tea
            sug = input("""We recommend these Food items with this product, Would you like to purchase?
00. Turkey Ham Sandwich
01. TUna Sandwich
02. None
Input: """)
            sukli = 0
            if sug == "00":
                turkeytea = turkey + tea
                if money_in > turkeytea:
                    print('Dispensing a Turkey Ham Sandwich and a Can of Tea')
                    sukli = money_in - turkeytea
                    print(sukli)
                elif turkeytea > money_in:
                    remain =  turkeytea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                tunatea = tuna + tea
                if money_in > tunatea:
                    print('Dispensing a Tuna Sandwich and a Can of Tea')
                    sukli = money_in - tunatea
                    print(sukli)
                elif tunatea > money_in:
                    remain = tunatea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "02":
                change = money_in - coke                    
                print("\nDispensing Can of Tea")
                print("Your change is" , change)
         else:
            remain = tea - money_in
            print("Cash insufficient. Amount pending:", remain)


    #Food
    def A2():
         if money_in >= doritos:
            change = money_in - doritos
            sug = input("""We recommend these Drinks with this product, Would you like to purchase?
00. Water
01. Pepsi
02. Sprite
03. Coke
04. None
Input: """)
            sukli = 0
            if sug == "00":
                doriwater = doritos + water
                if money_in > doriwater:
                    print('Dispensing a Bag of Doritos and a Bottle of Water')
                    sukli = money_in - doriwater
                    print(sukli)
                elif doriwater > money_in:
                    remain = doriwater - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                doripepsi = doritos + pepsi
                if money_in > doripepsi:
                    print('Dispensing a Bag of Doritos and a Can of Pepsi')
                    sukli = money_in - pepsi
                    print(sukli)
                elif doripepsi > money_in:
                    remain = doripepsi - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            
            elif sug == "02":
                dorisprite = doritos + sprite
                if money_in > dorisprite:
                    print('Dispensing a Bag of Doritos and a Can of Sprite')
                    sukli = money_in - dorisprite
                    print(sukli)
                elif dorisprite > money_in:
                    remain =  dorisprite - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
                
            elif sug == "03":
                doricoke = doritos + coke
                if money_in > doricoke:
                    print('Dispensing a Bag of Doritos and a Can of Coke')
                    sukli = money_in - doricoke
                    print(sukli)
                elif doricoke > money_in:
                    remain =  doricoke - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "04":
                change = money_in - coke                    
                print("\nDispensing Can of Tea")
                print("Your change is" , change)
         else:
            remain = doritos - money_in
            print("Cash insufficient. Amount pending:", remain)

    def B2():
         if money_in >= lays:
            change = money_in - lays
            sug = input("""We recommend these Drinks with this product, Would you like to purchase?
00. Water
01. Pepsi
02. Sprite
03. Coke
04. None
Input: """)
            sukli = 0
            if sug == "00":
                layswater = lays + water
                if money_in > layswater:
                    print('Dispensing a Bag of Lays and a Bottle of water')
                    sukli = money_in - layswater
                    print(sukli)
                elif layswater > money_in:
                    remain = layswater - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                layspepsi = lays + pepsi
                if money_in > layspepsi:
                    print('Dispensing a Bag of Lays and a Can of Pepsi')
                    sukli = money_in - layspepsi
                    print(sukli)
                elif lays > money_in:
                    remain = layspepsi - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
            
            elif sug == "02":
                layssprite = lays + sprite
                if money_in > layssprite:
                    print('Dispensing a Bag of Lays and a Can of Sprite')
                    sukli = money_in - layssprite
                    print(sukli)
                elif layssprite > money_in:
                    remain = layssprite - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))
                
            elif sug == "03":
                layscoke = lays + coke
                if money_in > layscoke:
                    print('Dispensing a Bag of Lays and a Can of Coke')
                    sukli = money_in - layscoke
                    print(sukli)
                elif layscoke > money_in:
                    remain = layscoke - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "04":
                change = money_in - coke                    
                print("\nDispensing Can of Tea")
                print("Your change is" , change)
         else:
            remain = lays - money_in
            print("Cash insufficient. Amount pending:", remain)

    def C2():
         if money_in >= croissant:
            change = money_in - croissant
            change = money_in - coffee
            sug = input("""We recommend these Drinks with this product, Would you like to purchase?
00. Tea
01. Coffee
02. None
Input: """)
            sukli = 0
            if sug == "00":
                crosstea = croissant + tea
                if money_in > crosstea:
                    print('Dispensing a Croissant and a Can of Tea')
                    sukli = money_in - crosstea
                    print(sukli)
                elif crosstea > money_in:
                    remain = crosstea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                croscoffee = croissant + coffee
                if money_in > croscoffee:
                    print('Dispensing a Croissant and a Can of Coffee')
                    sukli = money_in - croscoffee
                    print(sukli)
                elif croscoffee > money_in:
                    remain = croscoffee - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "02":
                change = money_in - croissant                 
                print("\nDispensing a Croissant")
                print("Your change is" , change)
         else:
            remain = croissant - money_in
            print("Cash insufficient. Amount pending:", remain)

    def D2():
         if money_in >= muffin:
            change = money_in - muffin
            sug = input("""We recommend these Drinks with this product, Would you like to purchase?
00. Tea
01. Coffee
02. None
Input: """)
            sukli = 0
            if sug == "00":
                mufftea = muffin + tea
                if money_in > mufftea:
                    print('Dispensing a Muffin and a Can of Tea')
                    sukli = money_in - muffin
                    print(sukli)
                elif mufftea > money_in:
                    remain = mufftea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                muffcoffee = muffin + coffee
                if money_in > muffcoffee:
                    print('Dispensing a Muffin and a Can of Coffee')
                    sukli = money_in - muffcoffee
                    print(sukli)
                elif muffcoffee > money_in:
                    remain = muffcoffee - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "02":
                change = money_in - muffin                
                print("\nDispensing a Muffin")
                print("Your change is" , change)
         else:
            remain = muffin - money_in
            print("Cash insufficient. Amount pending:", remain)
        
    def E2():
         if money_in >= turkey:
            change = money_in - turkey
            sug = input("""We recommend these Drinks with this product, Would you like to purchase?
00. Tea
01. Water
02. None
Input: """)
            sukli = 0
            if sug == "00":
                turtea = turkey + tea
                if money_in > turtea:
                    print('Dispensing a Turkey Ham Sandwich and a Can of Tea')
                    sukli = money_in - turkey
                    print(sukli)
                elif turtea > money_in:
                    remain = turtea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                turwater = turkey + water
                if money_in > turwater:
                    print('Dispensing a Turkey Ham Sandwich and a Bottle of Water')
                    sukli = money_in - turtea
                    print(sukli)
                elif turtea > money_in:
                    remain = turtea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "02":
                change = money_in - turkey                
                print("\nDispensing a Turkey Ham Sandwich")
                print("Your change is" , change)
         else:
            remain = turkey - money_in
            print("Cash insufficient. Amount pending:", remain)

    def F2():
         if money_in >= tuna:
            change = money_in - tuna
            sug = input("""We recommend these Drinks with this product, Would you like to purchase?
00. Tea
01. Water
02. None
Input: """)
            sukli = 0
            if sug == "00":
                tunatea = tuna + tea
                if money_in > tunatea:
                    print('Dispensing a Tuna Sandwich and a Can of Tea')
                    sukli = money_in - tuna
                    print(sukli)
                elif tunatea > money_in:
                    remain = tunatea - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "01":
                tunawater = tuna + water
                if money_in > tunawater:
                    print('Dispensing a Tuna Sandwich and a Bottle of Water')
                    sukli = money_in - tunatea
                    print(sukli)
                elif tunawater > money_in:
                    remain = tunawater - money_in 
                    print('\nAmount pending', remain)
                    extra_money = int(input('Insert pending money: '))
                    sukli = extra_money - remain
                    print('Your change is: '+ str(sukli))

            elif sug == "02":
                change = money_in - tuna                
                print("\nDispensing a Tuna Sandwich")
                print("Your change is" , change)
         else:
            remain = tuna - money_in
            print("Cash insufficient. Amount pending:", remain)


            

    time.sleep(1)   

    if prdct_code == "A1":
        A1()
    elif prdct_code == "B1":
        B1()
    elif prdct_code == "C1":
        C1()
    elif prdct_code == "D1":
        D1()
    elif prdct_code == "E1":
        E1()
    elif prdct_code == "F1":
        F1()
    elif prdct_code == "A2":
        A2()
    elif prdct_code == "B2":
        B2()
    elif prdct_code == "C2":
        C2()
    elif prdct_code == "D2":
        D2()
    elif prdct_code == "E2":
        E2()
    elif prdct_code == "F2":
        F2()
    else:
        print('Code Invalid')
    
    time.sleep(1)
    if que == False:
        q = input('''\nWould you like to continue?
Input Yes to continue
Input No to quit:
''')
        if q == 'Yes':
            que = False
        elif q == 'No':
            que = True
            print('Thank you for purchasing')

#Conditional statement using if elif to match the product code, each statement runs the function
