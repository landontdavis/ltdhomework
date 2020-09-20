# Notes
'''
#data set
data=[9, 41, 12, 3, 74, 15]

#first part of the problem
print('before data set')
for thing in data:
    print(thing)
print('after data set')

#if statement to find largest number in set with flag value to start
lsf=None
print('before largest number', lsf)
for num in data:
    if lsf is None or num>lsf:
        lsf=num
    print(lsf,num)
print('after largest number',lsf)
'''

#working on the exercise
largest=None
smallest=None
while True:
    number=input('Enter a number: ')
    if number=='done':
        break
    elif number.isnumeric()==False:
        print("Invalid input")
        continue
    elif number.isnumeric():    
        number=int(number)
        if largest is None or number>largest:
            largest=number
        if smallest is None or number<smallest:
            smallest=number
print('Maximum is',largest)
print('Minimum is',smallest)


# Christian's version

largest=None
smallest=None
while True:
    number=input('Enter a number: ')
    if number=='done':
        break
    elif number.isnumeric()==False:
        print("Invalid input")
        continue
    elif number == None:
        continue
    elif number.isnumeric():
        number = int(number)  
        if largest == None or number>largest:
            largest=number
        if smallest == None or number<smallest:
            smallest=number
print('Maximum is',largest)
print('Minimum is',smallest)


