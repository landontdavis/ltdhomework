# Notes from videos
'''
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average=sum(numlist) / len(numlist)
print('Average: ', average)


a=[1,2,3]
b=[4,5,6]
c=a+b
print(len(c))
'''


text=input("Enter file name: ")
try:
    fh=open(text)
except:
    print('File cannot be opened:',text)
    exit()

file=open(text)
a=[]
for a in file:
    x=a.split()
    if x[a][0].isupper():
        list.append(x[a])
    x.pop(a)

newlist=list+x

print(newlist)   
