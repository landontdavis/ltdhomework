#Prompt user for hours and rate per hours
hrs=input("Enter Hours:")
rate=input("Enter Rate:")

#Convert to float
hrs=float(hrs)
rate=float(rate)

#Work out the payrate
pay=hrs*rate

#output
print("Pay:",pay)
