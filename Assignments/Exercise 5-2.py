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
    while True:
        try:
            number=int(number)
            break
        except ValueError:
            print('Invalid input')
            continue
    if largest is None or number>largest:
            largest=number
    if smallest is None or number<smallest:
            smallest=number
print('Maximum is',largest)
print('Minimum is',smallest)

'''
 while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
'''




# Christian's version

number = ''
largest=None
smallest=None
while True:
    number=input('Enter a number: ')
    if number=='done':
        break
    try :
        number_ = int(number)
    except :
        print('Invalid input')
        continue
    if largest == None or number_>largest:
        largest=number_
    if smallest == None or number_<smallest:
        smallest=number_
print('Maximum is',largest)
print('Minimum is',smallest)


