my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
import random
def generate_random(row, column):
    sayılistesi=[]
    for i in range(0,256):
        sayılistesi.append(i)
    renkler=["red","green","blue"]
    deger=random.choices(sayılistesi,k=(row*column)*3)
    deger1=[deger[i:i+3] for i in range(0,len(deger),3)]
    deger2=[deger1[i:i+row] for i in range(0,len(deger1),row)]
    sayı=0
    sayı_1=0
    sözlüklist=[]
    for i in range(0,column):
        for a in range(0,row):
            b=deger2[sayı][sayı_1]
            zipli = zip(renkler, b)
            sayı_1=sayı_1+1
            zipli_1=dict(zipli)
            sözlüklist.append(zipli_1)
        sayı_1=0
        sayı=sayı+1
    sözlüklist=[sözlüklist[i:i+row] for i in range(0,len(sözlüklist),row)]
    return sözlüklist
def is_valid(img):
    bos=[]
    bos1=[]
    bos2=[]
    for ab in img:
        for ba in ab:
            a=ba["red"]
            b=ba["green"]
            c=ba["blue"]
            bos.append(a)
            bos.append(b)
            bos.append(c)
    for i in bos:
        if type(i)!=int:
            return False
        else:
            bos1.append(i)
    for a in bos1:
        if a<0:
            bos2.append(a)
        elif a>255:
            bos2.append(a)
    if len(bos2)==0:
        return True
    else:
        return False
def mirror_x(img):
    kopya=img.copy()
    img.clear()
    for i in kopya:
        i=i[::-1]
        img.append(i)
    return None
def mirror_y(img):
    kopyay=img.copy()
    img.clear()
    kop=kopyay[::-1]
    for i in kop:
        img.append(i)
    print(kop)
    return None
def clear(img):
    for i in img:
        for a in i:
            a["red"]=0
            a["green"]=0
            a["blue"]=0
    return None
def set_value(img, value, channel='rgb'):
    if value>255 or value<0:
        return "Geçersiz değer.Değerler [0,255] aralığında olmalıdır."
    else:
        c1=list(channel)
        for i in c1:
            if i=="r":
                for i in img:
                    for a in i:
                        a["red"]=value
            elif i=="g":
                for i in img:
                    for a in i:
                        a["green"]=value
            elif i=="b":
                for i in img:
                    for a in i:
                        a["blue"]=value
        return None
def fix(img):
    if is_valid(img)==False:
        for ab in img:
            for ba in ab:
                a=ba["red"]
                b=ba["green"]
                c=ba["blue"]
                if type(a)!=int or type(b)!=int or type(c)!=int:
                    if type(a)!=int:
                        ba["red"]=round(a)
                    elif type(b)!=int:
                        print("Burdayım")
                        ba["green"]=round(b)
                    elif type(c)!=int:
                        ba["blue"]=round(c)
        for ab in img:
            for ba in ab:
                a=ba["red"]
                b=ba["green"]
                c=ba["blue"]
                if a>255 :
                    ba["red"]=255
                elif a<0:
                    ba["red"]=0
                elif b<0 :
                    ba["green"]=0
                elif b>255:
                    ba["green"]=255
                elif c<0 :
                    ba["blue"]=0
                elif c>255:
                    ba["blue"]=255 
    return None
def rotate90(img):
    newboard=list(zip(*img))           
    newboard1=[l[::-1] for l in newboard]
    newboard1 = [list(ele) for ele in newboard1]
    return newboard1
def rotate180(img):
    im1=rotate90(img)
    im2=rotate90(im1)
    return im2
def rotate270(img):
    im1=rotate90(img)
    im2=rotate90(im1)
    im3=rotate90(im2)
    return im3                
def enhance(img, value, channel='rgb'):
    ch=list(channel)
    for i in ch:
        if i == "r":
            for ab in img:
                for ba in ab:
                    a=ba["red"]
                    ba["red"]=round(value*a)
        if i=="g":
            for ab in img:
                for ba in ab:
                    b=ba["green"]
                    ba["green"]=round(b*value)
        if i =="b":
            for ab in img:
                for ba in ab:
                    c=ba["blue"]
                    ba["blue"]=round(c*value)
        fix(img)
    return None
def write_to_file(img, filename):
    boslist=[]
    for ab in img:
        for ba in ab:
            a1=ba["red"]
            a2=ba["green"]
            a3=ba["blue"]
            boslist.append(a1)
            boslist.append(a2)
            boslist.append(a3)
    dosya=open(filename,"w")
    bosstr=""
    baska=list(zip(*[iter(boslist)]*3))
    bos1=[]
    for i in baska:
        for ab in i:
            c=hex(ab)
            c=c[2:]
            if len(c)==1:
                c="0"+c
            bosstr=bosstr+c
        bos1.append(bosstr)
        bosstr=""
    bos1_1=list(zip(*[iter(bos1)]*len(img)))
    bos5=[]
    boss=""
    sayı=0
    for i in bos1_1:
        for v in i:
            a=i[sayı]
            boss=boss+","+v
            sayı=sayı+1
        sayı=0
        bos5.append(boss[1:])
        boss=""
    bos6=list(bos5)
    for a in list(bos5):
        
        dosya.write(a)
        dosya.write("\n")
        
    return None
    
def read_from_file(filename):
    try:
        dosya=open(filename)
        dos=dosya.readlines()
        bos=[]
        bos1=[]
        for i in dos:
            bos.append(i)
    except FileNotFoundError:
        return "Hatalı Dosya Adı Girdiniz."
    kacsatır=len(bos[0][:-1])
    for i in bos:
        bos1.append(i[:-1])
    row=len(bos1)
    asillist=[]
    for i in bos1:
        ab=i.split(",")
        asillist.append(ab)
    column=len(asillist[0])
    listeyeter=[]
    for ab in asillist:
        for i in ab:
            print(i)
            a=int(i[0:2],16)
            b=int(i[2:4],16)
            c=int(i[4:6],16)
            listeyeter.append(a)
            listeyeter.append(b)
            listeyeter.append(c)
    renkler=["red","green","blue"]
    deger1=[listeyeter[i:i+3] for i in range(0,len(listeyeter),3)]
    deger2=[deger1[i:i+row] for i in range(0,len(deger1),row)]
    sayı=0
    sayı_1=0
    sözlüklist=[]
    for i in range(0,column):
        for a in range(0,row):
            b=deger2[sayı][sayı_1]
            zipli = zip(renkler, b)
            sayı_1=sayı_1+1
            zipli_1=dict(zipli)
            sözlüklist.append(zipli_1)
        sayı_1=0
        sayı=sayı+1
    sözlüklist=[sözlüklist[i:i+row] for i in range(0,len(sözlüklist),row)]
    return sözlüklist
def grayscale(img, mode=1):
    if mode==1:
        for ab in img:
            for ba in ab:
                a=ba["red"]
                b=ba["green"]
                c=ba["blue"]
                d=round((a+b+c)/3)
                ba["red"]=d
                ba["green"]=d
                ba["blue"]=d
    elif mode==2:
        for ab in img:
            for ba in ab:
                a=ba["red"]
                b=ba["green"]
                c=ba["blue"]
                ba["red"]=round( 0.299*a)
                ba["green"]=round(0.587*b)
                ba["blue"]=round(0.114*c)
    elif mode==3:
        for ab in img:
            for ba in ab:
                a=ba["red"]
                b=ba["green"]
                c=ba["blue"]
                ba["red"]=round( 0.2126*a)
                ba["green"]=round(0.7152*b)
                ba["blue"]=round(0.0722*c)
    elif mode==4:
        for ab in img:
            for ba in ab:
                a=ba["red"]
                b=ba["green"]
                c=ba["blue"]
                ba["red"]=round( 0.2627*a)
                ba["green"]=round(0.6780*b)
                ba["blue"]=round(0.0593*c)
    return None
def get_freq(img, channel='rgb',bin_size=16):
    list1=[]
    for i in range(0,256):
        list1.append(i)
    liste2=[]
    liste3=[]
    sayı=0
    for i in range(0,int(256/bin_size)):
        for i in range(0,bin_size):
            liste2.append(list1[sayı])
            sayı=sayı+1
        liste3_1=liste2.copy()
        liste3.append(liste3_1)
        liste2.clear()
    k1=len(liste3)
    k1_1=[]
    for a in range(0,k1):
        k1_1.append(0)
    red=k1_1.copy()
    green=k1_1.copy()
    blue=k1_1.copy()
    ifade=list(channel)
    for i in ifade:
        if i == "r":
            for ab in img:
                for ba in ab:
                     a=ba["red"]
                     sayı1=0
                     for i in range(0,len(liste3)):
                         a1=liste3[sayı1]
                         if a in a1:
                             break
                         else:
                             sayı1=sayı1+1
                     red[sayı1]=red[sayı1]+1
        elif i == "g":
            for ab in img:
                for ba in ab:
                     a=ba["green"]
                     sayı1=0
                     for i in range(0,len(liste3)):
                         a1=liste3[sayı1]
                         if a in a1:
                             break
                         else:
                             sayı1=sayı1+1
                     green[sayı1]=green[sayı1]+1
    for i in ifade:
        if i == "b":
            for ab in img:
                for ba in ab:
                     a=ba["blue"]
                     sayı1=0
                     for i in range(0,len(liste3)):
                         a1=liste3[sayı1]
                         if a in a1:
                             break
                         else:
                             sayı1=sayı1+1
                     blue[sayı1]=blue[sayı1]+1
    sözlük={"bin_size":bin_size,"red":red,"green":green,"blue":blue} 
    return sözlük
def scale_up(img,N):
    bos1=[]
    bos2=[]
    for ab in img:
        for ba in ab:
            for i in range(0,N):
                bos1.append(ba)
    a1=(len(img[0])*N)
    list1=[bos1[i:i+a1] for i in range(0,len(bos1),a1)]
    print(list1)
    for i in list1:
        for a in range(0,N):
            bos2.append(i)
    return bos2
            
def scale_down(orig, N):
    pass
def apply_window(orig2, w):
    pass


    