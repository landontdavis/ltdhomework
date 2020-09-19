#Prompt user for hours and rate per hours
hrs=input("Enter Hours:")
rate=input("Enter Rate:")

#Convert to float
hrs=float(hrs)
rate=float(rate)

#How much to pay
if hrs<=40:
    pay=rate*hrs
else:
    pay=(40*rate)+(1.5*rate*(hrs-40))
print(pay)
