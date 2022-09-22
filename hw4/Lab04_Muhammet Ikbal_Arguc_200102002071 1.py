my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"

#Problem1
def problem1(x,y):
    if len(x)-1<y:
        return None
    elif y<0:
        return None
    else:
        return x[y]
#Problem2
def problem2(x,y):
    uzunluk=len(x)-1
    if y<0:
       return x
    elif y>uzunluk:
        return x
    else:
        x.pop(y)
        return x 
#problem3
def problem3(x,y):
    x=list(x)
    if y==True:
        x.sort()
        return x
    elif y==False:
        x.sort()
        return x[::-1]
#Problem4
def problem4(x,y):
    sayı=0
    yenix= list(set(x))
    yeniy= list(set(y))
    for i in yenix:
        if i in yeniy:
            sayı=sayı+1
        else:
            sayı=sayı+0
    return sayı
#Problem5
def problem5(a,b):
    indeks=0
    indeks1=0
    toplam=0
    carpım=0
    toplam1=0
    for i in range(0,len(a)):
        carpım=(a[indeks]*b[indeks])
        toplam=toplam+carpım
        indeks=indeks+1
    for i in range(0,len(b)):
        toplam1=b[indeks1]+toplam1
        indeks1=indeks1+1
    return float(toplam/toplam1)
#Problem6
def problem6(v):
    if len(v)==1:
        return float(v[0][0])
    if len(v[0])!=len(v[1]):
        return None
    else:
        if len(v[0])==2:
            if len(v)!=2:
                return None
            else:
                sonuc1=((v[0][0])*(v[1][1])-(v[0][1])*(v[1][0]))
                return float(sonuc1)
        elif len(v[0])==3:
            if len(v)!=3:
                return None
            else:
                if len(v[0])==len(v[1]) and len(v[1])==len(v[2]):
                    a1=(((v[0][0])*(v[1][1])*(v[2][2]))+((v[1][0])*(v[2][1])*(v[0][2]))+((v[2][0])*(v[0][1])*(v[1][2])))
                    a2=(((v[0][2])*(v[1][1])*(v[2][0]))+((v[1][2])*(v[2][1])*(v[0][0]))+((v[2][2])*(v[0][1])*(v[1][0])))
                    return float(a1-a2)
                else:
                    return None
        elif len(v[0])==4:
            if len(v)!=4:
                return None
            else:
                
                if len(v[0])==len(v[1]) and len(v[1])==len(v[2]) and len(v[2])==len(v[3]):
                    b1=(((v[1][1])*(v[2][2])*(v[3][3]))+((v[2][1])*(v[3][2])*(v[1][3]))+((v[3][1])*(v[1][2])*(v[2][3])))
                    b_1=(((v[1][3])*(v[2][2])*(v[3][1]))+((v[2][3])*(v[3][2])*(v[1][1]))+((v[3][3])*(v[1][2])*(v[2][1])))
                    b1t=float(+1*(v[0][0])*(b1-b_1))
                    b2=(((v[1][0])*(v[2][2])*(v[3][3]))+((v[2][0])*(v[3][2])*(v[1][3]))+((v[3][0])*(v[1][2])*(v[2][3])))
                    b_2=(((v[1][3])*(v[2][2])*(v[3][0]))+((v[2][3])*(v[3][2])*(v[1][0]))+((v[3][3])*(v[1][2])*(v[2][0])))
                    b2t=float(-1*(v[0][1])*(b2-b_2))
                    b3=(((v[1][0])*(v[2][1])*(v[3][3]))+((v[2][0])*(v[3][1])*(v[1][3]))+((v[3][0])*(v[1][1])*(v[2][3])))
                    b_3=(((v[1][3])*(v[2][1])*(v[3][0]))+((v[2][3])*(v[3][1])*(v[1][0]))+((v[3][3])*(v[1][1])*(v[2][0])))
                    b3t=float(+1*(v[0][2])*(b3-b_3))
                    b4=(((v[1][0])*(v[2][1])*(v[3][2]))+((v[2][0])*(v[3][1])*(v[1][2]))+((v[3][0])*(v[1][1])*(v[2][2])))
                    b_4=(((v[1][2])*(v[2][1])*(v[3][0]))+((v[2][2])*(v[3][1])*(v[1][0]))+((v[3][2])*(v[1][1])*(v[2][0])))
                    b4t=float(-1*(v[0][3])*(b4-b_4))
                    toplam=b1t+b2t+b3t+b4t
                    return float(toplam)           
                else:
                    return None
#Problem7
def problem7(accounts,source,lira,kurus):
    kurusnew=kurus*(10**-2)
    para=(int(lira)+kurusnew)
    if source<0:
        return accounts
    elif source>(len(accounts)-1):
        return accounts
    else:
        fiyat=accounts[source]
        fiyat1=float(fiyat)-float(para)
        if float(fiyat1)==int(fiyat1):           
            fiyat2=str(fiyat1)
        else:
            fiyat2="%.2f" % fiyat1
        
        if float(fiyat1)<0:
            return accounts
        else:
            accounts.pop(source)
            accounts.insert(source,fiyat2)
            return accounts
#Problem8
def problem8(accounts,source,destination,lira,kurus,fee=False):
    kurusnew1=kurus*(10**-2)
    kurusnew1=float("{:.2f}".format(kurusnew1))
    para=(int(lira)+kurusnew1)
    if fee==False:
        if source<0:
            return accounts
        elif source>(len(accounts)-1):
            return accounts
        elif source==destination:
            return accounts
        else:
            a1=float(accounts[source])
            a2=float(accounts[destination])
            a3=float(a1)-float(para)#hesapta yeterı kadar para var mı
            a4=float(a2)+float(para)
            a31=("{:.2f}".format(a3))
            a41=("{:.2f}".format(a4))
            if a3<0:
                return accounts
            else:
                if int(a3)==float(a3) and int(a4)!=float(a4):
                    accounts.pop(source)
                    accounts.insert(source,str(a3))
                    accounts.pop(destination)
                    accounts.insert(destination,(a41))
                    return accounts
                elif int(a3)!=float(a3) and int(a4)==float(a4):
                    accounts.pop(source)
                    accounts.insert(source,(a31))
                    accounts.pop(destination)
                    accounts.insert(destination,str(a4))
                    return accounts
                elif int(a3)==float(a3) and int(a4)==float(a4):
                    accounts.pop(source)
                    accounts.insert(source,str(a3))
                    accounts.pop(destination)
                    accounts.insert(destination,str(a4))
                    return accounts
                else:
                    accounts.pop(source)
                    accounts.insert(source,a31)
                    accounts.pop(destination)
                    accounts.insert(destination,a41)
                    return accounts
    if fee==True:
        if source<0:
            return accounts
        elif source>(len(accounts)-1):
            return accounts
        elif source==destination:
            return accounts
        else:
            if para<10:
                para1=para+0.1
            else:
                fee2=para*1/100
                fee2format="{:.2f}".format(fee2)
                para1=para+float(fee2format)
            b1=float(accounts[source])
            b2=float(accounts[destination])
            b3=float(b1-para1)
            b4=float(b2+para)
            b41=float("{:.2f}".format(b4))
            b31=float("{:.2f}".format(b3))
            b4_1=("{:.2f}".format(b4))
            b3_1=("{:.2f}".format(b3))
            if b3<0:
                return accounts
            else:
                if int(b3)==float(b3) and int(b4)!=float(b4):
                    accounts.pop(source)
                    accounts.insert(source,str(b3))
                    accounts.pop(destination)
                    accounts.insert(destination,(b4_1))
                    return accounts
                elif int(b3)!=float(b3) and int(b4)==float(b4):
                    accounts.pop(source)
                    accounts.insert(source,(b3_1))
                    accounts.pop(destination)
                    accounts.insert(destination,str(b4))
                    return accounts
                elif int(b3)==float(b3) and int(b4)==float(b4):
                    accounts.pop(source)
                    accounts.insert(source,str(b3))
                    accounts.pop(destination)
                    accounts.insert(destination,str(b4))
                    return accounts
                else:
                    accounts.pop(source)
                    accounts.insert(source,(b3_1))
                    accounts.pop(destination)
                    accounts.insert(destination,(b4_1))
                    return accounts
#Problem9
def problem9():
    pass
#Problem10
def problem10(c):
    indeks10=0
    ifade=[]
    for i in range(0,len(c)):
        deger=c[indeks10]
        
        c.pop(indeks10)
        
        if deger in c:
            ifade.append(deger)
            
    if len(ifade)>0:
        yeni=list(set(ifade))
        return ",".join(yeni)
    else:
        return None
    
    
        
            
                             
            
        
            
            