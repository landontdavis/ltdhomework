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
    if fnum=='done':break
    elif fnum 
    for x in fnum:
        if largest is None or x>largest:
            largest=x
    for y in fnum:
        if smallest in None or y<smallest:
            smallest=y
    print(fnum)
print('Maximum is',largest)
print('Minimum is',smallest)
