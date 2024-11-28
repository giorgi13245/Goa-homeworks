#or ოპერატორის შემთხვევაში შედარება დაგვიბრუნებს True როდესაც გამოსახულებაში ერთ-ერთი პირობა სრულდება and ოპერატორის შემთხვევაში კი ყველა პირობა უნდა შესრულდეს


#(True or False)=True (True or True)=True (False or True)=True (False or False)=False
#(True and False)=False (True and True)=True (False and True)=False (False and False)=False


name=input("please enter your name")
age=int(input("please enter your age"))
print(age>=18 or name=="giorgi")