#.append გამოიყენება სიაში ელემენტის ჩასამატებლად
#.insert გამოიყენება სიაში მითითებულ ინდექსზე ელემენტის ჩასამატებლად
#.pop გამოიყენება სიიდან ელემენტის ამოსაგდებად
#len გამოიყენება სიაში ან სტრინგში ელემენტებისა და სიმბოლოების რაოდენობის გამოსატანად
#.upper გამოიყენება სტრინგში ყველა ასოს გასადიდებლად
#.lower გამოიყენება სტრინგში ყველა ასოს დასაპატარავებლად
#.capitalize გამოიყენება სტრინგში პირველი ასოს გასადიდებლად და დანარჩენის დასაპატარავებლად
#.find გამოიყენება სტრინგში გარკვეული სიმბოლოს მოსაძებნად


names=["ახალაია",'მაისურაძე','ხელაძე','ლაბაძე','ბოყოველი']
name=input('enter your name')
if len(name)>7:
    names.append(name)
    print(names)
else:
    print("invalid")




list=['s','a','b','l','f','e','p','m','n','c']
print(list[::2])



fruit="mango"
print(len(fruit))


name1=input('enter your name in upper schrift for example:GIORGI:')
name1=name1.lower()
print(name1)




last_name='boyoveli'
last_name=last_name.upper()
print(last_name)




sport='football'
sport=sport.capitalize()
print(sport)