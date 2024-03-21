from catdom1 import Cat

Cat1 = Cat("Барон", "male", 2)
Cat2 = Cat("Сэм", "male", 2)

print("Name first cat: ", Cat1.name)
print("Gender first cat: ", Cat1.gender)
print("Age first cat: ", Cat1.age)


print("----------------")


print("Name second cat: ", Cat2.cat_name())
print("Gender second cat: ", Cat2.cat_gender())
print("Age second cat: ", Cat2.cat_age())
