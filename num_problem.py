#Question:Write a program which will find all such numbers which are divisible by 'n' but are not a multiple of 'y',between 'a' and 'b' (both included).
a=int(input('enter lower range:'))
b=int(input('enter a upper range:'))
n=int(input('enter divisible:'))
y=int(input('enter a but not multiple:'))
out=[]
while(b>=a):
    b=b-1
    if(b%n==0):
        if(b%y!=0):
            out.append(b)
print(out)
