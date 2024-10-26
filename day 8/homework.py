print(2>1)
print(3>1)
print(8>19)

print(4<8)
print(23<54)
print(34<23)

print(23>=23)
print(34>=21)
print(18>=25)

print(60<=60)
print(72<=98)
print(84<=47)

print(23==7)
print(38==94)
print(45==45)

number=int(input("please enter your favourite number"))
print(number==5)

print(True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5)
#     True or False and True or True and False and True
#           
#True or False and 5 > 3 or "name" == "name" and 123 =="123" and 5 >= 5  გარდაიქმნება True or False and True or True and False and True რაც მოგვცემს True-ს





surname=input("enter your surname")
age=int(input("enter your age" ))
print(surname=="boyoveli" or age>=18)


#ალგორითმი არის ნაბიჯ-ნაბიჯ დაწერილი ინსტრუქცია რომელიც ზუსტად თანმიმდევრობით უნდა შესრულდეს გარკვეული დავალების შესასრულებლად, ალგორითმის მაგალითებია:კერძის რეცეპტი,ლეგოს ასაწყობი ინსტრუქცია,დანიშნულებამდე მისასვლელი მიმართულებები


#ალგორითმის გამოსახვის ხერხებია:flowchart-ი ფოტოთი ალგორითმის გამოსახვა,ფსევდო კოდი:ალგორითმის გამოსახვა, რომელიც იყენებს ნატურალური ენას და პროგრამირების ელემენტებს და natural language: როდესაც კომპიუტერისთვის გასაგები ენით ხსნი შენს ალგორითმს.

#controll flow-ს აქვს სამი ტექნიკა:sequencing-კოდის თანმიმდევრობით გაშვება iteration-ერთიდაიგივე მოქმედების ბევრჯერ გამეორება, selection-არჩევა

num1=int(input("enter number N1"))
num2=int(input("enter number N2"))
num3=int(input("enter number N3"))
num4=int(input("enter number N4"))
num5=int(input("enter number N5"))
average=(num1+num2+num3+num4+num5)/5
print(average<num1*num5)