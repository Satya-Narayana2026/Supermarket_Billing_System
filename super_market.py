from datetime import datetime

name = input("Enter Your Name:")


# LISTS OF ITEMS

lists = '''


Rice         Rs 48/kg
Sugar        Rs 45/kg
Salt         Rs 30/kg
Oil          Rs 180/liter
Ata          Rs 45/kg
Maggi        Rs 50/kg
Boost        Rs 90/each
Horlicks     Rs 90/each
Colagate     Rs 85/each
Milk         Rs 35/each
Coffee       Rs 20/each
Biscuits     Rs 20/each
Brush        Rs 30/each


'''
# DECLERATION

price = 0
price_list=[]
total_price = 0
final_price = 0
ilist = []
qlist = []
plist = []

# RATES FOR ITEMS

items = {'rice':48,
         'sugar':45,
         'salt':30,
         'oil':180,
         'ata':45,
         'maggi':50,
         'boost':90,
         'horlicks':90,
         'colgate':85,
         'milk':35,
         'coffee':20,
         'biscuits':20,
         'brush':30
           }

option = int(input("Press 1 for list of items :"))

if option == 1:
    print(lists)

for i in range(len(items)):
    inp1 = int(input("If you want to buy press 1 or 2 for exit :"))

    if inp1 == 2:
        break

    if inp1 == 1:
        item = input("Enter Your items :").lower()
        quantity = int(input("Enter  Quantity :"))

        if item  in items.keys():
            price = quantity*(items[item])
            price_list.append((item, quantity, items[item], price))
            total_price += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (total_price*5)/100
            final_amount = gst+total_price
        else:
            print("Sorry You Entered Item is Not Available")
    else:
        print("You Entered Wrong Option")

    
inp = input("Can I Generate The Bill yes or no :").lower()
if inp == 'yes':
    pass

    if final_amount != 0:
        print(25*"=","Satya Supermarket",25*"=")
        print()
        print(28*" ","Hyderabad")
        print()
        print("Name:",name)
        print("Date:",datetime.now())
        print(75*"-")
        print(f"{'S.No':<6}{'Item':<15}{'Quantity':<12}{'Price':<10}")


        for i in range(len(price_list)):
            print(f"{i+1:<5}{ilist[i]:<15}{qlist[i]:<10}{plist[i]:<10}")


        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',total_price)
        print("gst amount",50*" ",'Rs',gst)
        print(50*" ",'final_amount:','Rs',final_amount)
        print(75*"-")
        print(25*" ","THANKS FOR VISITING")
        print(75*"-")