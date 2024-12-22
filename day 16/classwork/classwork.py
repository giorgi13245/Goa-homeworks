name=input("enter your name")
name_type=input("choose how to write you name:upper,lower or capitalised:")
name_type=name_type.lower()

if name_type=="upper":
    print(name.upper)
elif name_type=="lower":
    print(name.lower)
elif name_type=="capitalised":
    print(name.capitalize)






surname=input("enter surname:")
if surname.find("shvili")>0:
    print("როგორ ხარ?")
elif surname.find("ia")>0:
    print("მუჭო რექ?")
else:
    print("bye")


names=["nia","giorgi","lado","nika"]
name1=input("enter name")
name1=name1.lower
if name1[0]=="d" and name1[-1]=='i':
    print(names.append(name1))
    print(names)
else:
    print("invalid")



list1=['a','b','c','d','e','f','g','h','i','j']
index=int(input("enter number between 0-9"))
list1.pop(index)
print(list1)



food=['potato','carrot','apple','grape','banana']
index1=int(input("enter number between 0-4"))
fav_food=input("enter your favorite food")
food.insert(index1,fav_food)



