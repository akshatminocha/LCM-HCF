#HCF
def gcd(a,b):
    if(a==b):
        smaller=a
    elif(a<b):
        smaller=a
    elif(a>b):
        smaller=b
    for i in range(1,smaller+1):
        if((a%i==0) and (b%i==0)):
            g=i
    return g
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("GCD of",x,"and",y,"is",gcd(x,y))
