# Collins Wanga

foodCharge=eval(input("enter the food charge:  "))
tip=foodCharge*0.18
print(format(tip, '.2f'))
salesTax=foodCharge*0.07
print(format(salesTax, '.2f'))
total=foodCharge+tip+salesTax
print(format(total, '.2f'))
