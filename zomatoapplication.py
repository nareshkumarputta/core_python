class zomato:
    discount=0.20
    coupon_code='zomato70x'
    lor={'mehfil','paradise','bawarchi'}
    restuarent_number=0
    def __init__(self,restuarent_name):
        self.restuarent_name=restuarent_name
        self.item={
                    1: {"name": "Pizza", "price": 250},
                    2: {"name": "Burger", "price": 150},
                    3: {"name": "Pasta", "price": 200},
                    4: {"name": "Sandwich", "price": 120},
                    5: {"name": "French Fries", "price": 100},
                    6: {"name": "Noodles", "price": 180},
                    7: {"name": "Egg_Biryani", "price": 250},
                    8: {"name": "Chicken Wings", "price": 300},
                    9: {"name": "Ice Cream", "price": 80},
                    10:{"name": "Cold Drink", "price": 50},
                    11:{"name":"chicken_biryani","price":560},
                    12:{"name":"mutton_biryani","price":780}}
        zomato.restuarent_number+=1
        self.restuarent_id=zomato.restuarent_number
        if restuarent_name in zomato.lor:
            print("Menu List:")
            for key,value in self.item.items():
                    print(f"{key}:{value}")
        else:
            print("Restuarent not available")
    def order(self,n):
        if n in self.item:
            print("Your Selected Item is:",self.item[n]['name'])
            self.price=self.item[n]['price']
            p=input("Enter Your Coupon Code:")
            if p==zomato.coupon_code:
                self.price=self.price-self.price*zomato.discount
                print("Your Final Bill After Applied Discount:",self.price)
            else:
                print(f"Your Bill for item {self.item[n]['name']} is: {self.item[n]['price']}")
        else:
            print("Item Not Avaialable in The Menu")

r=input("enter your restuarent name:")
obj1=zomato(r)
if obj1.restuarent_name in zomato.lor:
    n=int(input("Select Your Order:"))
    obj1.order(n)

# class Swiggy:
#     rest_names = set({})
#     rno = 0
#     discount = 0.2
#     coupon = "Happy"
#     def __init__(self, rname, ritems):
#         Swiggy.rno += 1
#         self.rid = Swiggy.rno
#         self.rname = rname
#         Swiggy.rest_names.add(rname)
#         self.ritems = ritems
# Paradise = Swiggy("Paradise", {"Chicken Biryani": 120, "Mutton Biryani" : 200})
# Mehfil = Swiggy("Mehfil",{"Chicken Biryani": 220, "Mutton Biryani" : 200})
# # print(Swiggy.rest_names)
# c = 0
# for i in Swiggy.rest_names:
#     c += 1
#     print(c, i)
# choice = int(input("Enter the Choice"))
# c = 0
# if choice == 1:
#     for i in Mehfil.ritems.items():
#         c += 1
#         print(c, i)

        
