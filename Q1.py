##Q1) Write a simple program that will read the input r which indicate redies of the circle and calculate the area and the circumference of that circle ?

#Area = pi * r ^2

#Cir = Pi * 2 * r

pi= 3.14
r= int(input("please enter\n"))
if r>=0:
    A= pi*r**2
    C=pi*2*r
    print(A)
    print(C)
else:
    print("entered wrong nyumber")