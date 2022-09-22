#!/usr/bin/env python3
# -*- coding: utf-8 -*-
my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"

#Problem1
def problem1():
    my_name="İkbal"
    indexname=my_name[0]
    return indexname
#Problem2
def problem2():
    my_name="İkbal"
    ab=len(my_name)
    num=int(input("Enter a number: "))
    num2=num%ab
    islem=my_name[num2]
    return islem 
#Problem3
def problem3():
    isim="İkbal"
    deger10=int(input("Enter first number: "))
    deger20=int(input("Enter second number: "))
    deger1_1=deger10%5
    deger2_2=deger20%5
    if deger1_1<deger2_2:
        islem2=isim[deger1_1:deger2_2]
    elif deger2_2<deger1_1:
        islem2=isim[deger2_2:deger1_1]
        
    return islem2
#Problem4
def problem4():
    s=input("Enter input: ")
    ss=s.replace(" ", "")
    x= 0
    if len(ss)>100 or len(ss)<1:
        return
    else:
        for char in s:
            if char in ["a", "e","i", "o", "u","U","A","E","I","O"]:
                x += 1
            elif char not in ["a", "e","i", "o", "u","U","A","E","I","O"]:
                x=x+0
        return x
#Problem5
def problem5():
    my_id="200102002071"
    sayı=0
    for i in my_id:
        sayı+=int(i)
    return sayı

#Problem6
def problem6():
    number1=int(input("Enter input: "))
    fac=1
    if number1<=30:
        for i in range(1,number1+1):
            fac=fac*i
        return fac
    else:
        return
#Problem7
def problem7():
    number2=int(input("Enter a number: "))
    a=(number2%3)
    b=(number2%7)
    c=a==b
    if number2>=0:
        
        if a==b:
            return bool(c)
        else:
            return bool(c)
    else:
        return
#Problem8
def problem8():
    ab=int(input("Enter a number: "))
    das=0
    if ab>=0:
        
        if ab%3==0 and ab%7!=0:
            das=das+1
            return das
        elif ab%7==0 and ab%3!=0:
            das=das+2
            return das
        elif ab%7==0 and ab%3==0:
            das=das+3
            return das
    else:
        return
#Problem9
def problem9():
    prime_num=int(input("Enter a number: "))
    
    if prime_num>1:
        for i in range(2,prime_num):
            if prime_num%i==0:
                return False
        return True
    else:
        return
    
#Problem10

def problem10():
    kök=float(input("Enter a number: "))
    if kök==0:
        return 0
    g=kök/2
    fark=1
    x22=0.000000001
    while fark>x22:
        kök1=0.5*(g+(kök/g))
        fark=g-kök1
        g=kök1
    return g


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



    
    
        
        
    

    

        
    
        
               
           
           
           
    
    