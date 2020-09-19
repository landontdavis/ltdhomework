#Prompt user for score
score=input("Enter Score: ")

#Float Number
x=Float(score)

#Conditional Statement
if x>1:
    print("Error! Please input a number between 0.0 and 1.0")
elif x>=0.9:
    print("A")
elif x>=0.8:
    print("B")
elif x>=0.7:
    print("C")
elif x>=0.6:
    print("D")
elif x<0.6 and x>=0:
    print("F")
else:
    print("Error! Please input a number between 0.0 and 1.0")
