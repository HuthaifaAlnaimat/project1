#Q2) write a program to calculate summation of the numbers from n to m for example the summation of when n=3 and m=9 is  3+4+5+6+....9 = 42 ?

#Note: n should be always less than m



#inputs
#n and m
#if statement
#n<=m
#sum the num from 3 to 9
#for from i in range (n,m)

n=int(input())
m=int(input())
sum=0
if n<=m:
    for i in range (n,m+1):
        sum=sum+i
        i+=1
print(sum)