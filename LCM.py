#LCM
def lcm(a,b):
    if(a>b):
        larger=a
    else:
        larger=b
    while(a>0 or b>0):
        if((larger%a==0) and (larger%b==0)):
            l=larger
            break
        larger+=1
    return l
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("LCM of",x,"and",y,"is",lcm(x,y))
