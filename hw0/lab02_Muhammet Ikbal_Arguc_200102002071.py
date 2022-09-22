#!/usr/bin/env python3
# -*- coding: utf-8 -*-
my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"


#Problem 1
def problem1():
    name="Hi all, This is Muhammet İkbal Arğuç!"
    return name

#Problem 2
def problem2():
    write=str(input("Enter some input: "))
    write1="Input was "+write
    return write1


#Problem 3
def problem3():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    add=num1+num2
    return add

#Problem 4
def problem4():
    firstnum=float(input("Enter first number: "))
    secondnum=float(input("Enter second number: "))
    sub=firstnum-secondnum
    return sub

#Problem 5
def problem5():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number :"))
    modulo=a%b
    return modulo
#Problem 6
def problem6():
    radius=float(input("Enter radius: "))
    height=float(input("Enter height: "))
    pi=3.141592
    volume=(radius**2)*(height)*pi
    return volume
#Problem 7
def problem7():
    one_side=float(input("Enter one side: "))
    value=4*one_side
    abc="The perimeter of the square is "+str(value)+"."
    return abc



if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
    print("-----------------------------------")
    print("problem1 working...")
    print(problem1())
    print("-----------------------------------")
    
    print("problem2 working...")
    print(problem2())
    print("-----------------------------------")
    
    print("problem3 working...")
    print(problem3())
    print("-----------------------------------")
    
    print("problem4 working..")
    print(problem4())
    print("-----------------------------------")
    
    print("problem5 working...")
    print(problem5())
    print("-----------------------------------")
    
    print("problem6 working...")
    print(problem6())
    print("-----------------------------------")
    print("problem7 working...")
    print(problem7())
    