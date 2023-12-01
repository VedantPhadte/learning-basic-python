print("enter your weight")
weight = float(input())
x = input("convert in (k)g or (l)bs :")
if(x =="k" or x == "K"):   # or use x.upper() == "K"
    print("weight=",weight//2.22,"kg")
elif(x == "l" or x == "L"):
    print("weight=",weight*2.22,"lbs")
else:
    print("invalid option")
print("original weight=",weight)