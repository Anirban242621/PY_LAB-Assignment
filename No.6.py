#Write a program to calculate simple interest for a given principal, rate of interest, and time. 
a = int(input("Enter principal amount:"))
b = int(input("Enter duration of loan:"))
c = int(input("Enter rate of interest:"))
d = a*b*c/100
print("Total Interest: ",d)
