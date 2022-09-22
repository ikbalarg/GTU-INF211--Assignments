my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
#Problem1
def problem1(liste,sayı):
    a_liste=list(dict.fromkeys(liste))
    bos_liste=[]
    for i in a_liste:
        say=liste.count(i)
        if say==sayı:
            bos_liste.append(i)
    return bos_liste
#Problem2
def problem2(girdi):
    icsayı=len(girdi)
    if icsayı==0:
        return 0
    elif icsayı%2==1:
        listem=list(girdi.values())
        listem.sort()
        return listem[int(len(listem)/2)]
    else:
        listem=list(girdi.values())
        listem.sort()
        a=int(len(listem)/2)
        b=a-1
        return int((listem[b]+listem[a])/2)
#Problem3
def problem3(filename):
    sayı=0
    try:
        open(filename)
        liste1=["name","credit","term","grade"]
        liste=[]
        a_file = open(filename)   
        boşliste=[]
    except FileNotFoundError:
        return []
    for i in a_file:
        l = i.strip().split(',')
        liste.append(l)
    for i in liste:
        if i[3]=="":
            i[3]="NA"
    say=0
    for b in range(0,len(liste)):
        liste[say][1]=int(liste[say][1])
        liste[say][2]=int(liste[say][2])
        say=say+1
    for a in range(0,len(liste)):
        zipli=zip(liste1,liste[sayı])
        a_dictionary = dict(zipli)
        d1=a_dictionary.copy()
        boşliste.append(d1)
        sayı=sayı+1
    return boşliste   
#Problem4
def problem4(sözlük,term1):
    sayı=0
    sayı1=0
    notlar=[]
    krediler=[]
    sayısalNot=[]
    kreditoplam=0
    nottoplam=0
    terms=[]
    if len(sözlük)==0:
        return 0
    else:
        for i in range(0,len(sözlük)):
            terms.append(sözlük[sayı]["term"])
            if sözlük[sayı]["grade"]!="NA":
                if sözlük[sayı]["term"]==term1:
                    a=sözlük[sayı]["credit"]
                    b=sözlük[sayı]["grade"]
                    krediler.append(a)
                    notlar.append(b)
            sayı=sayı+1
        for i in notlar:
            if i == "NA":
                kacıncı=notlar.index("NA")
                krediler.pop(kacıncı)                
            elif i=="BA":
                 sayısalNot.append(3.5)
            elif i=="BB":
                sayısalNot.append(3.0)
            elif i=="CB":
                sayısalNot.append(2.5)
            elif i=="CC":
               sayısalNot.append(2.0)
            elif i=="DC":
                sayısalNot.append(1.5)
            elif i=="DD":
                sayısalNot.append(1.0)
            elif i=="FF":
                sayısalNot.append(0.0)
            elif i=="AA":
                sayısalNot.append(4.0)
        if term1 not in terms:
            return 0
        for b in range(0,len(sayısalNot)):
            a1=sayısalNot[sayı1]
            b1=krediler[sayı1]
            kreditoplam=kreditoplam+float(b1)
            nottoplam=nottoplam+(float(a1)*float(b1))
            sayı1=sayı1+1
        return float(nottoplam/kreditoplam)
#Problem5
def problem5(fonksiyon,deger5):
    boş=[]
    baska=[]
    strin=""
    for i in range(0,deger5+1):
        boş.append(str(i))
    for i in boş:
        if "1" in i:
            baska.append(int(i))
            strin=strin+i
    deger5_1=fonksiyon(deger5)
    return deger5_1==strin.count("1")
#Problem6
def problem6(text):
    bos=[]
    text=str(text)
    text=text.lower()
    res = [text[i: j] for i in range(len(text)) 
          for j in range(i + 1, len(text) + 1)]
    for i in res:
        if len(i)>1:
            for c in i:
                 for perm in problem6(i.replace(c,'',1)):
                     bos.append(c+perm)
        elif len(i)==1:
            bos.append(i)
    bos1 = list(dict.fromkeys(bos))
    bos1.sort()
    return bos1
#Problem7
def problem7(text,file1):
    kombinasyonlar=problem6(text)
    ortaklar=[]
    with open(file1,"r") as reader:
        ac=reader.read().splitlines()
    for i in kombinasyonlar:
        if i in ac:
            ortaklar.append(i)
    ortaklar.sort()
    return  ortaklar
#Problem8
def problem8(liste1,liste2):
    lis = liste1
    row = len(liste1)
    column = len(liste1[0])
    count=0
    x = 0
    bos=[]
    while x < row:
        y = x+1
        while y <= row:
            a = 0
            while a < column:
                b = a+1
                while b <= column:
                    altmat = []
                    for i in lis[x:y]:
                        altmat.append(i[a:b])
                    
                    bos.append(altmat)
                    count += 1
                    b += 1
                a += 1
            y += 1
        x += 1
    return liste2 in bos
#Problem9
def problem9(girdi):
    islem1=len(girdi)
    string=""
    tekrarsız = "".join(dict.fromkeys(girdi))
    for i in tekrarsız:
        a=girdi.count(i)
        if a==1:
            string=string+i
        elif a!=1:
            string=string+i+str(a)
    islem2=len(string)
    islem3=((islem1-islem2)*100)/islem1
    return (string,round(islem3))
#Problem10
def problem10(liste10):
    maxi=max(liste10)
    mini=min(liste10)
    bos_liste10=[]
    olmayan=[]

    for i in range(mini,maxi+1):
        bos_liste10.append(i)

    for a in bos_liste10:
        if a not in liste10:
            olmayan.append(a)
    if len(olmayan)==0:
        return int(maxi+1)
    else:
        return int(olmayan[0])