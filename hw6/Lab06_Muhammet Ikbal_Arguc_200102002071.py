my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
#Problem1
def problem1():
    class p1:
        def __init__(self,x):
            self.a=x
        def get_value(self):
            if type(self.a)==int:
                return self.a
            else:
                self.a=0
                return 0
        def set_value(self,x):
            if type(x)==int:
                self.a=x
       
    return p1
#Problem2
def problem2():
    class p1:
        def __init__(self,x,y):
            self.x=x
            self.y=y
        def get_area(self):
            return self.x*self.y
        def get_perimeter(self):
            return (2*self.x)+(2*self.y)
    return p1
#Problem3
def problem3():
    class Grades:
        def __init__(self):
            self.a=[]
        def add_grade(self,x):
            self.a.append(x)
        def remove_grade(self,x):
            try:
                self.a.remove(x)
            except ValueError:
                bos=1
        def get_min(self):
            if len(self.a)==0:
                return 0.0
            else:
                return float(min(self.a))
        def get_max(self):
            if len(self.a)==0:
                return 0.0
            else:
                return float(max(self.a))
        def get_mean(self):
            a=len(self.a)
            if a!=0:
                b=0
                for i in self.a:
                    b=b+i
                return float(b/a)
            else:
                return 0.0
        def get_median(self):
            a1=len(self.a)
            self.a.sort()
            if a1!=0:
                return float((sum(self.a[a1//2-1:a1//2+1])/2.0, self.a[a1//2])[a1 % 2]) if a1 else None
            else:
                return 0.0
    return Grades
#Problem4
def problem4():
    class Movie:
        def __init__(self,movie_name,director,year,rating,length):
            self.movie_name=movie_name
            self.director=director
            self.year=year
            self.rating=rating
            self.length=length
        def get_movie_name(self):
            return str(self.movie_name)
        def get_director(self):
            return str(self.director)
        def  get_year(self):
            return int(self.year)
        def get_rating(self):
            return float(self.rating)
        def get_length(self):
            return  int(self.length)
        def set_rating(self,x):
            if x>=0.0 and x<=10.0:
                x=self.raiting
        def set_length(self,x):
            if type(x)==int:
                if x>=0 and x<=500:
                    x=self.length
    return Movie
#Problem5
def problem5():
    class MovieCatalog:
        def __init__(self,filename):
            try:
                dosya=open(filename)
                dos=dosya.readlines()
                filmler=[]
                filmler1=[]
            except FileNotFoundError:
                print("Dosya Bulunamadı..")
            for i in dos:
                filmler.append(i[:-1])
                film=filmler.copy()
                filmler1.append(film)
                filmler.clear()
            listem=[]
            for a in filmler1:
                for i in a:
                    i=i.split(",")
                    listem.append(i)            
            pro_list=[]
            pl=[]
            for i in listem:
                x=i[0]
                y=i[1]
                z=i[2]
                x1=i[3]
                y1=i[4]
                a=problem4()(x,y,z,x1,y1).get_movie_name()
                a10=problem4()(x,y,z,x1,y1).get_director()
                a20=problem4()(x,y,z,x1,y1).get_year()
                a30=problem4()(x,y,z,x1,y1).get_rating()
                a40=problem4()(x,y,z,x1,y1).get_length()
                pro_list.append(a)
                pro_list.append(a10)
                pro_list.append(a20)
                pro_list.append(a30)
                pro_list.append(a40)
                a11=pro_list.copy()
                pl.append(a11)
                pro_list.clear()
            self.filename=pl
            print(self.filename)
        def add_movie(self,movie_name, director, year, rating=0.0, length=0):
            list1=[movie_name,director,year,rating,length]
            if list1 not in self.filename:
                self.filename.append(list1)
        def remove_movie(self,movie_name) :
            for i in self.filename:
               if i[0]==movie_name:
                    self.filename.remove(i)
        def get_oldest(self):
            list1=[]
            for i in self.filename:
                list1.append(i[2])
            a=min(list1)
            for i in self.filename:
                if a==i[2]:
                    return i[0]
        def get_lowest_ranking(self):
            list1=[]
            for i in self.filename:
                list1.append(i[3])
            a=min(list1)
            for i in self.filename:
                if a==i[3]:
                    return i[0]
        def get_highest_ranking(self):
            list1=[]
            for i in self.filename:
                list1.append(i[3])
            a=max(list1)
            for i in self.filename:
                if a==i[3]:
                    return i[0]
        def get_by_director(self,director):
            list1=[]
            for i in self.filename:
                if director==i[1]:
                    list1.append(i[0])
            return list1
    return MovieCatalog
#Problem6
import random
def problem6():
    class Node:
        def __init__(self,x,y,z):
            if x==None and y==None and z==None:
                self.x=random.randint(-20,20)
                self.y=random.randint(-20,20)
                self.z=random.randint(-20,20)
            else:
                self.x=x
                self.y=y
                self.z=z
        def get_node(self):
            return (self.x,self.y,self.z)
        def get_distance(self):
            return (((self.x**2)+(self.y**2)+(self.z**2))**(0.5))
        def __add__(self,other):
            yenix=self.x+other.x
            yeniy=self.y+other.y
            yeniz=self.z+other.z
            return Node(yenix,yeniy,yeniz)
        def __str__(self):
            return "<"+str(self.x)+","+str(self.y)+","+str(self.z)+">"
        def __gt__(self,other):
            a=(self.x+self.y+self.z)
            b=(other.x+other.y+other.z)
            return a>b
        def  __ge__ (self,other):
            a=(self.x+self.y+self.z)
            b=(other.x+other.y+other.z)
            return a>=b
        def __lt__(self,other):
            a=(self.x+self.y+self.z)
            b=(other.x+other.y+other.z)
            return a<b
        def __le__(self,other):
            a=(self.x+self.y+self.z)
            b=(other.x+other.y+other.z)
            return a<=b
        def __eq__(self,other):
            a=(self.x+self.y+self.z)
            b=(other.x+other.y+other.z)
            return a==b
    return Node
#Problem7
def problem7():
    class  NodeCloud:
        def __init__(self,n):
            #(n), and this parameter is used to tell how many Nodes there are in the Node Cloud.
            self.n=n 
            bos=[]
            for i in range(0,self.n):
                N = problem6()
                ninst1 = N(None, None, None)
                bos.append(ninst1.get_node())
            self.b=bos
        
        def get_nodes(self):
            return self.b
        def get_outermost(self):
            b=[]
            for i in self.b:
                a=(((i[0]**2)+(i[1]**2)+(i[2]**2))**0.5)
                b.append(a)
            a=b.index(max(b))
            return self.b[a]
        def add_node(self,x, y, z):
            ab=(x,y,z)
            if ab not in self.b:
                self.b.append(ab)
                self.n+1
        def get_sum(self):
            a=0
            b=0
            c=0
            for i in self.b:
                a=i[0]+a
                b=i[1]+b
                c=i[2]+c
            return problem6()(a,b,c)
    return NodeCloud
#Problem8
def problem8():
    class Encoder:
        def __init__(self,x):
            self.x=x
            new=""
            a1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for i in self.x:
                if i in a1:
                    new=new+i
            self.x=new
        def __str__(self):
            return str(self.x)
        def morse(self):
            bos=[]
            MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
            sel=self.x.upper()
            for i in sel:    
                bos.append(MORSE_CODE_DICT[i])
            return bos
        def binary(self):
            b=""
            for i in self.x:
                c=bin(ord(i))
                b=b+c[2:]
            return b
        def hex(self):
           return "".join("{:02x}".format(ord(c)) for c in self.x)
    return Encoder
