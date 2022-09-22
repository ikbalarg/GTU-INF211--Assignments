#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 18:03:08 2021

@author: ikbalarguc
"""
my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
#Problem1
def problem1():
    deger1=float(input("Enter Fahrenheit degree: "))
    cel=float((deger1-32)*(5/9))
    return cel
#Problem2
def problem2():
    deger2=float(input("Enter Celsius degree: "))
    fah=float(((deger2*9)/5)+32)
    return fah
#Problem3
def problem3():
    deger3=int(input("Enter a number: "))
    hexa=int(2*(deger3**2)-deger3)
    return hexa
#Problem4
def problem4():
    deger4=int(input("Enter a number: "))
    l0=2
    l1=1
    if deger4==0:
        return int(2)
    if deger4==1:
        return int(1)
    if deger4==2:
        return int(3)
    elif deger4>2:
        for i in range(1,deger4+1):
            ltoplam=l0+l1
            l0=l1
            l1=ltoplam
        return l0
#Problem5
def problem5():
    deger5=str(input("Enter a string: "))
    deger5_1=deger5.replace(" ", "")
    return deger5_1[::-1]
#Problem6
def problem6():
    deger6=str(input("Enter a string: "))
    deger6_1=deger6.replace(" ", "")
    olamaz=['!','#','$','%','&','/','(',')','*','+','-',',','.','\',',':',';',
                 '=','>','<','?','@','[',']','//','^','_','`','{','}','|','~','"',"'"]
    for i in olamaz:
        deger6_1=deger6_1.replace(i, "")
    return deger6_1

#Problem7
def problem7():
    deger7=int(input("Enter a number: "))
    ifade=""
    if deger7>=0:
        while True:
            if deger7==0:
                break
            ifade=ifade+str(deger7%4)
            deger7=deger7//4
            ters=(ifade[::-1])
        return ters
    elif deger7<0:
        deger7=deger7*(-1)
        while True:
            if deger7==0:
                break
            ifade=ifade+str(deger7%4)
            deger7=deger7//4
            ters=(ifade[::-1])
        return "-"+ters
#Problem8
def problem8():
    deger=str(input("Enter input: "))
      
    baslar = tuple('({[')
    sonlar = tuple(')}]')
    map = dict(zip(baslar, sonlar))
    bos = []
  
    for i in deger:
        if i in baslar:
            bos.append(map[i])
        elif i in sonlar:
            if not bos or i != bos.pop():
                return False
    if not bos:
        return True
    else:
        return False
#Problem9
def problem9():
    deger9=str(input("Enter a string: "))
    deger9_1=deger9.split(" ")
    lendeger9_1=len(deger9_1[-1])
    
    
    if len(deger9)<=200 and len(deger9)>=1:
        return lendeger9_1
    else:
        return
#Problem10
def problem10():
    deger10=input("Enter the exit route: ")
    yatay=0
    dikey=0
    for i in deger10:
        if i=="s":
            dikey=dikey-1
        elif i=="n":
            dikey=dikey+1
        elif i=="w":
            yatay=yatay-1
        elif i=="e":
            yatay=yatay+1
    uzunluk=(yatay)**2+(dikey)**2
    if uzunluk==0:
        return 0
    guess=0.0
    step=0.001
    eps=1E-9
    while True:
        if abs(guess*guess-uzunluk)<eps:
            break
        elif guess*guess>uzunluk:
            break
        guess+=step
    return guess
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
    print("-----------------------------------")
    print("problem8 working...")
    print(problem8())
    print("-----------------------------------")
    print("problem9 working...")
    print(problem9())
    print("-----------------------------------")
    print("problem10 working...")
    print(problem10())

        
            
            
            
        

    
            
        



        
        
        
        
        
