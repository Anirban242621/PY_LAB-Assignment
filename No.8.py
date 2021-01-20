#Two numbers are input through the keyboard into two location C and D. Write a program to interchange the contents of C and D.

a,b=input("Enter the value of C and D:").split()
t=b
b=a
a=t
print("The value of C and D:",a,b)

