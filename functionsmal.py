# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:23:50 2021

@author: admin
"""

def addition(a,b):
    c=a+b
    return c
def subtraction(a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
num1=int(input('Enter the first number:'))
num2=int(input('Enter the seond number:'))
print('\n1.addition \n2.subtraction \n3.multiplcation \n4.division')
choice=int(input('Enter your choice:'))
if(choice==1):
    add=addition(num1,num2)
    print(add)
elif(choice==2):
    sub=subtraction(num1,num2)
    print(sub)
elif(choice==3):
    mul=multiplication(num1,num2)
    print(mul)
elif(choice==4):
    div=division(num1,num2)
    print(div)
else:
    print("Enter a valid choice:")
