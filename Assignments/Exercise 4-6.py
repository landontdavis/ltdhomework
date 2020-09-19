#Exercise 4.6
# Def Code needed to run
def computepay(hrs,rate):
    pay=((hrs-40)*1.5*rate)+(40*rate)
    return pay

#Prompt user for hours and rate per hours
hrs=input("Enter Hours:")
rate=input("Enter Rate:")

#Convert to float
hrs=float(hrs)
rate=float(rate)

#Calculation

if hrs<=40:
    pay=rate*hrs
else:
    pay=computepay(hrs,rate)
print("Pay",pay)
