class zomato:
    discount=0.20
    coupon_code='zomato70x'
    lor={'mehfil','paradise','bawarchi'}
    restuarent_number=0
    def __init__(self,restuarent_name):
        self.restuarent_name=restuarent_name
        self.item={1:{'name':'chicken_biryani','price':300},
                    2:{'name':'mutton_biryani','price':650},
                    3:{'name':'coke','price':50}}
        zomato.restuarent_number+=1
        self.restuarent_id=zomato.restuarent_number
        if restuarent_name in zomato.lor:
            print("Menu List:")
            for key,value in self.item.items():
                    print(f"{key}:{value}")
        else:
            print("Enter a valid restuarent")
    def order(self,n):
        if n in self.item:
            self.price=self.item[n]['price']
            p=input("Enter Your Coupon Code:")
            if p==zomato.coupon_code:
                self.price=self.price-self.price*zomato.discount
                print("Your Final Bill After Applied Discount:",self.price)
            else:
                print(f"Your Bill for item {self.item[n]['name']} is: {self.item[n]['price']}")
        else:
            print("Invalid Item")

r=input("enter your restuarent name:")
obj1=zomato(r)
if obj1.restuarent_name in zomato.lor:
    n=int(input("Select Your Order:"))
    obj1.order(n)