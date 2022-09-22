#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 14:41:40 2021

@author: ikbalarguc
"""
my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
#Problem1
def problem1(x):
    if "K" in x:
        return True
    else:
        return False
        
#Problem2
def problem2(a,b,c,d):
    return float(min(a, b,c,d))
#Problem3
def problem3(x,y):
    if x==y:
        if x==0:
            return 0
        if x>0 and x<1 and y<1 and y>0:
            if y<0.5:
                return 0
            elif y>=0.5:
                return 1
        elif x<0 and x>-1 and y>-1 and y<0:
            if y<=-0.5:
                return -1
            elif y>-0.5:
                return 0
        elif x<0:
            if x<=int(x)-0.5:
                return int(x)-1
            else:
                return int(x)
        else:
            if x<int(x)+0.5:
                return int(x)
            else:
                return int(x)+1
    if x<y:
        if int(x)==x:
            return x
        else:
            if abs(x-y)<1:
                if x>0 and x<1 and y<1 and y>0:
                    if y<0.5:
                        return 0
                    elif y>=0.5:
                        return 1
                elif x<0 and x>-1 and y>-1 and y<0:
                    if y<=-0.5:
                        return -1
                    elif y>-0.5:
                        return 0
                elif x<0 and y<0:
                    if y>int(y)+0.5:
                        return int(y)
                    else:
                        return int(y)-1
            else:
                if x>0:
                    return int(x)+1
                elif x<0:
                    if y<0:
                        return int(x)-1
                    else:
                        return int(x)            
    elif x>y:
        if int(x)==x:
            return x
        else:
            if abs(x-y)<1:
                if y<0 and y>-1 and x<=0 and x>-1 :
                    if y>-0.5:
                        return 0     
                    elif y<=0.5:
                        return -1
                elif x>0 and x<1:
                    if y>=0.5:
                        return 1
                    else :
                        return 0
                elif y<0 and x<0:
                    if y<=int(y)-0.5:
                        return int(y)-1 #negatif
                    else:
                        return int(y)
                else:
                    if y<int(y)+0.5:
                        return int(x)  #pozitif
                    elif y>=int(y)+0.5:
                        return int(y)+1      
            elif abs(x-y)>=1:
                if x<0 and y<0:
                    return int(x)-1
                else:
                    return int(x)
#Problem4
def problem4(radius,height,pi=3.1415):
    return (radius**2)*height*pi
#Problem5
def problem5(radius,height,pi=3.1415):
    if type(radius) is int or (type(radius)==float) :
        if type(height) is int or (type(height)==float) :
            if type(pi) is int or (type(pi)== float):
               return (radius**2)*height*pi
            else:
                return -1
        else:
            return-1
            
    else:
        return -1
#Problem6
def problem6(h):
    h=h.replace(" ","")
    h1=",".join(h)
    listh=h1.split(",")
    listyedek=h1.split(",")
    ifade6=""
    sayı6=0
    for i in range(0,len(listh)):
        ifade6_1=listh[sayı6]
        listyedek.pop(sayı6)
        if ifade6_1 not in listyedek:
            ifade6=ifade6_1+ifade6
        listyedek.insert(sayı6, ifade6_1)
        sayı6=sayı6+1
    return ifade6[::-1]
#Problem7
def problem7(x):
    if x=="".join(sorted(x)):
        return True
    else:
        return False
#Problem8
def problem8(x):
    x=x.replace(" ","")
    x1=",".join(x)   
    listx=x1.split(",")
    yenilist=x1.split(",")
    sayıx=0
    for i in range(0,len(listx)):        
        ifade=listx[sayıx]
        yenilist.pop(sayıx)
        if ifade in yenilist:
            return False
    
        yenilist.insert(sayıx,ifade)
        sayıx=sayıx+1
    return True     
#Problem9
def problem9(row,column):
    if row==1 and column==1:
        return 1
    elif column==1 and row!=1:
        return 3
    elif column==row:
        return 2
    else: 
        return problem9(row-1,column-1)+problem9(row-1, column)   
#Problem10
def problem10(a,b):
    a=a.replace(" ","")
    b=b.replace(" ","")
    uzunluka=len(a)
    uzunlukb=len(b)
    a1=",".join(a)
    b1=",".join(b)
    lista=a1.split(",")
    listb=b1.split(",")
    sayı=0
    count=0
    if uzunluka>uzunlukb:
        for i in range(0,uzunlukb):
            if lista[sayı]==listb[sayı]:
                count=count+1
            sayı=sayı+1
        return count
    elif uzunluka==uzunlukb:
        for i in range(0,uzunlukb):
            if lista[sayı]==listb[sayı]:
                count=count+1
            sayı=sayı+1
        return count
    elif uzunluka<uzunlukb:
        for i in range(0,uzunluka):
            if lista[sayı]==listb[sayı]:
                count=count+1
            sayı=sayı+1
        return count        
        

               
           
        
            
            
            