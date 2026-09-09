def dec(func):
    def wrap(username,passw,first_call):
        func(username,passw,first_call)
        if username==name and passw==password:
            print("Authentication Successfull")
    return wrap
name='Naresh'
password=1234
usa=sa=0
@dec
def login(username,passw,first_call=True):
    global name,password,usa,sa
    if first_call:
        usa=0
    if username==name and passw==password:
        sa+=1
        print("Your Username is:",username)
        print("Your Password is:",password)
    elif username!=name and passw!=password:
        usa+=1
        if usa<3:
            login(input("enter your username again:"),int(input("enter your password again:")),False)
        else:
            print("You have Entered invallid credentials for 3 times")
            print("Your Account Has been Blocked")
            return usa,sa,username,password
    elif username!=name:
        usa+=1
        if usa<3:
            login(input("enter your username again:"),passw,False)
        else:
            print("You have Entered invallid credentials for 3 times")
            print("Your Account Has been Blocked")
            return usa,sa,username,password
    elif passw!=password:
            usa+=1
            if usa<3:
                login(username,int(input("enter your password again:")),False)
            else:
                print("You have Entered invallid credentials for 3 times")
                print("Your Account Has been Blocked")
                return usa,sa,username,password
n=input("enter your username:")
p=int(input("enter your password:"))
login(n,p,True)