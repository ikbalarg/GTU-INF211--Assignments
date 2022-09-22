my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
import random
class Person:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname         
    def get_name(self):
        return self.name+" "+self.lastname
    def __str__(self):
        return str(self.name)+" "+str(self.lastname)
    def __lt__(self,other):
        firstName=self.lastname
        secondName=other.lastname
        firstName1=self.name
        secondName1=other.name
        if firstName!=secondName:
            if firstName<secondName:
                return True
            else:
                return False
        elif firstName==secondName:
            if firstName1<secondName1:
                return True
            else:
                return False
class Player(Person):
    idCounter = 1
    isUnique=[]
    playerNames=[]
    def __init__(self,name,lastname):
        shootingPower=random.randint(4, 8)
        self.shoot=shootingPower
        self.name=name
        self.lastname=lastname
        self.oyuncu={"name":Person(name, lastname).get_name(),"id":None,"shooting power":self.shoot,"team":None,"points":[]}
        #print(self.oyuncu)
        if Person.get_name(self) not in Player.isUnique:
            Player.isUnique.append(Person.get_name(self))
            self.oyuncu["id"]=int(Player.idCounter)
            Player.idCounter+=1
            Player.playerNames.append(self.oyuncu)
        else:
            for i in Player.playerNames:
                if i["name"]==Person.get_name(self):
                    #print("Burdayım")
                    self.oyuncu["id"]=i["id"]
                    self.oyuncu["team"]=i["team"]
                    self.oyuncu["points"]=i["points"]
                    self.oyuncu["shooting power"]=i["shooting power"]
    def get_id(self):
        return self.oyuncu["id"]
    def get_power(self):
        return self.oyuncu["shooting power"]
    def get_team(self):
        return self.oyuncu["team"]
    def add_to_points(self,x):
        self.oyuncu["points"].append(x)
        return sum(self.oyuncu["points"])
    def get_points_detailed(self):
        return self.oyuncu["points"]
    def get_points(self):
        return sum(self.oyuncu["points"])
    def __lt__(self,other):
        toplam1=Player.get_points(self)
        toplam2=Player.get_points(other)
        if toplam1!=toplam2:
            return toplam2>toplam1
        else:
            return Person.__lt__(self, other)
    def reset(self):
        self.oyuncu["points"].clear()
    def set_team(self,t):
        t.players.append(self.oyuncu)
        t.detay.append(self.oyuncu)
        self.oyuncu["team"]=t
class Manager(Person):
    idCounter = 1
    isUniquem=[]
    managers=[]
    def __init__(self,name,lastname):
        Person.__init__(self, name, lastname)
        self.koc={"name":Person(name, lastname).get_name(),"id":Manager.idCounter,"team":None,"points":[]}
        if Person.get_name(self) not in Manager.isUniquem:
            Manager.isUniquem.append(Person.get_name(self))
            self.koc["id"]=int(Manager.idCounter)
            Manager.idCounter+=1
            Manager.managers.append(self.koc)
        else:
            for i in Manager.managers:
                if i["name"]==Person.get_name(self):
                    #print("Burdayım")
                    self.koc["id"]=i["id"]
                    self.koc["team"]=i["team"]
                    self.koc["points"]=i["points"]
    def reset(self):
        self.koc["points"].clear()
    def get_id(self):
        return self.koc["id"]
    def set_team(self,t):
        #t.takım["managerdetay"]["team"]=t
        self.koc["team"]=t
    def get_team(self):
        return self.koc["team"]
    def set_team(self,t):
        t.takım["managerdetay"]=self.koc
        self.koc["team"]=t
    def get_influence_detailed(self):
        return self.koc["points"]
    def get_influence(self):
        return sum(self.koc["points"])
    def __lt__(self,other):
        toplam1=Manager.get_influence(self)
        toplam2=Manager.get_influence(other)
        if toplam1!=toplam2:
            return toplam2>toplam1
        else:
            return Person.__lt__(self, other)
    def reset(self):
        self.koc["points"].clear()
class Team(Manager,Player):
    idCounter = 1
    isUniquet=[]
    teams=[]
    instances=[]
    def __init__(self,teamname,manager,players):
        self.teamname=teamname
        #print(self.teamname)
        self.manager=manager
        self.players=[]
        self.player1=players
        self.detay=[]
        self.fik=None
        self.__class__.instances.append(self)
        for i in self.player1:
            i.oyuncu["team"]=Team.instances.copy()[0]
            self.detay.append(i)
        self.manager.koc["team"]=Team.instances.copy()[0]
        for i in players:
            self.players.append(i.get_name())
        self.takım={"name":teamname,"manager":manager.get_name(),"players":self.players,"points":{"atılan":[],"yenilen":[]}
                    ,"detay":self.detay,"managerdetay":self.manager.koc,"fikstür":{}}
        #print(self.takım)
        if self.teamname not in Team.isUniquet:
            Team.isUniquet.append(self.teamname)
            self.takım["id"]=int(Team.idCounter)
            Team.idCounter+=1
            Team.teams.append(self.takım)
        else:
            for i in Team.teams:
                if i["name"]==self.teamname:
                    #print("Burdayım")
                    self.takım["id"]=i["id"]
                    self.takım["manager"]=i["manager"]
                    self.takım["players"]=i["players"]
                    self.takım["points"]=i["points"]
        Team.instances.clear()
    def get_name(self):
        return self.teamname
    def get_id(self):
        return self.takım["id"]
    def get_roster(self):
        list1=[]
        for i in self.player1:
            list1.append(i)
        return list1
    def __str__(self):
        return self.teamname
    def get_manager(self):
        return self.manager
    def get_scored(self):
        return sum(self.takım["points"]["atılan"])
    def get_conceded(self):
        return sum(self.takım["points"]["yenilen"])
    def add_result(self,s):
        sözlük={"atılan":s[0],"yenilen":s[1]}
        self.takım["galibiyet"].append(sözlük)
        self.takım["points"]["atılan"].append(s[0])
        self.takım["points"]["yenilen"].append(s[1])
    def get_wins(self):
        coun1=0
        galibiyet=0
        #print(self.takım["points"])
        for i in range(len(self.takım["points"]["atılan"])):
            a=self.takım["points"]["atılan"][coun1]
            b=self.takım["points"]["yenilen"][coun1]
            coun1+=1
            if a>b:
                galibiyet+=1
        return galibiyet
                
    def get_losses(self):
        coun1=0
        maglubiyet=0
        #print(self.takım["points"])
        for i in range(len(self.takım["points"]["atılan"])):
            a=self.takım["points"]["atılan"][coun1]
            b=self.takım["points"]["yenilen"][coun1]
            coun1+=1
            if b>a:
                maglubiyet+=1
        return maglubiyet
    def __lt__(self,other):
        ilkTakım=sum(self.takım["points"]["atılan"])
        ikinciTakım=sum(other.takım["points"]["atılan"])
        averaj1=sum(self.takım["points"]["atılan"])-sum(self.takım["points"]["yenilen"])
        averaj2=sum(other.takım["points"]["atılan"])-sum(other.takım["points"]["yenilen"])
        if ilkTakım!=ikinciTakım:
            #print("Burdayım")
            return ilkTakım<ikinciTakım
        elif ilkTakım==ikinciTakım:
            if averaj1!=averaj2:
                #print(averaj1,averaj2)
                return averaj1<averaj2
            elif averaj1==averaj2:
                #print("eşit")
                return True
    def reset(self):
        for i in self.takım["detay"]:
            i.oyuncu["points"].clear()
        self.takım["points"]["atılan"].clear()
        self.takım["points"]["yenilen"].clear()
        self.takım["managerdetay"]["points"].clear()
        self.takım["fikstür"].clear()
        #fikstür temizle
    def add_to_fixture(self,m):
        self.takım["fikstür"][m.fik[0]]=m.fik[1]
        sorted_keys = sorted(list(self.takım["fikstür"].keys()), key = lambda x: (len(x),x))
        sorted_dict = {k:self.takım["fikstür"][k] for k in sorted_keys}
        #self.takım["fikstür"]={k:self.takım["fikstür"][k] for k in sorted(self.takım["fikstür"])}
        self.takım["fikstür"]=sorted_dict
    #self.takım["fikstür"][0]={k:self.takım["fikstür"][0][k] for k in sorted(self.takım["fikstür"][0])}
    def get_fixture(self):
        #self.takım["fikstür"]={k:self.takım["fikstür"][k] for k in sorted(self.takım["fikstür"])}
        values = self.takım["fikstür"].values()
        values_list = list(values)
        return values_list
class Match(Team,Player):
    instance=[]
    def __init__(self,home_team, away_team,week_no):
        self.home_team=home_team
        self.away_team=away_team
        self.week_no=week_no
        #print(self.home_team.detay)
        self.__class__.instance.append(self)
        self.score=None
        self.winner=None
        self.isplayed=False
        strİfade=str(self.week_no)+".Hafta"
        self.homeTeamFixture=[strİfade,Match.instance.copy()[0]]
        self.home_team.fik=self.homeTeamFixture
        self.away_team.fik=self.homeTeamFixture
        Match.instance.clear()
    def get_teams(self):
        #print(Team.get_name(self.home_team))
        return ((self.home_team),(self.away_team))
    def get_home_team(self):
        return self.home_team
    def get_away_team(self):
        return self.away_team
    def play(self):
        listhome=[]
        listaway=[]
        home_manager_point =int(random.randint(-10, 10))
        away_manager_point =int(random.randint(-10, 10))
        self.home_team.takım["managerdetay"]["points"].append(home_manager_point)
        self.away_team.takım["managerdetay"]["points"].append(away_manager_point)
        
        for i in self.home_team.takım["detay"]:
            a=i.oyuncu["shooting power"]
            l1=[]
            
            for a in range(0,4):
                x=random.randint(-5, 5)
                l1.append(x+a)
               
            l2=l1.copy()
            #i.oyuncu["points"].append(sum(l2))
            i.add_to_points(sum(l2))
            listhome.append(sum(l2))
            l1.clear()
        for i in self.away_team.takım["detay"]:
            a=i.oyuncu["shooting power"]
            l3=[]
            for a in range(0,4):
                x=random.randint(-5, 5)
                l3.append(x+a)
            l4=l3.copy()
            i.add_to_points(sum(l4))
            #i.oyuncu["points"].append(sum(l4))
            listaway.append(sum(l4))
            l3.clear()
        homeScore=home_manager_point+sum(listhome)
        awayScore=away_manager_point+sum(listaway)
        #print(homeScore,awayScore)
        if homeScore==awayScore:
            while homeScore==awayScore:
                for i in self.home_team.takım["detay"]:
                    #print("Eşitlik Oldu")
                    a=i.oyuncu["shooting power"]
                    l1=[]
                    for a in range(0,1):
                        x=random.randint(-5, 5)
                        l1.append(x+a)
                    l2=l1.copy()
                    i.add_to_points(sum(l2))
                    #i.oyuncu["points"].append(sum(l2))
                    listhome.append(sum(l2))
                    l1.clear()
                for i in self.away_team.takım["detay"]:
                    a=i.oyuncu["shooting power"]
                    l3=[]
                    for a in range(0,1):
                        x=random.randint(-5, 5)
                        l3.append(x+a)
                    l4=l3.copy()
                    i.add_to_points(sum(l4))
                    #i.oyuncu["points"].append(sum(l4))
                    listaway.append(sum(l4))
                    l3.clear()
                for i in self.home_team.takım["detay"]:
                    
                    a=i.oyuncu["points"][-1]
                    b=i.oyuncu["points"][-2]
                    del i.oyuncu["points"][-1]
                    del i.oyuncu["points"][-1]
                    i.oyuncu["points"].append(a+b)
                for i in self.away_team.takım["detay"]:
                   
                    a=i.oyuncu["points"][-1]
                    b=i.oyuncu["points"][-2]
                    del i.oyuncu["points"][-1]
                    del i.oyuncu["points"][-1]
                    i.oyuncu["points"].append(a+b)
                homeScore=home_manager_point+sum(listhome)
                awayScore=away_manager_point+sum(listaway)
                #print(homeScore,awayScore)
        self.home_team.takım["points"]["atılan"].append(sum(listhome.copy())+home_manager_point)
        self.home_team.takım["points"]["yenilen"].append(sum(listaway.copy())+away_manager_point)
        self.away_team.takım["points"]["atılan"].append(sum(listaway.copy())+away_manager_point)
        self.away_team.takım["points"]["yenilen"].append(sum(listhome.copy())+home_manager_point)
        """print(self.home_team.takım["points"]["atılan"],self.home_team.takım["points"]["yenilen"])
        print(self.away_team.takım["points"]["atılan"],self.away_team.takım["points"]["yenilen"])
        print(home_manager_point,away_manager_point)"""
        #for i in home_team.takım
        listhome.clear()
        listaway.clear()
        #print(homeScore,awayScore)
        self.score=homeScore,awayScore
        #print(self.score)
        self.isplayed=True
        if homeScore>awayScore:
            self.winner=self.home_team
        elif homeScore<awayScore:
            self.winner=self.away_team
        return None
    def get_match_score(self):
        return self.score
    def get_winner(self):
        if self.isplayed==True:
            return self.winner
        elif self.isplayed==False:
            return None
    def is_played(self):
        return self.isplayed
    def __str__(self):
        if self.isplayed==False:
            return Team.get_name(self.home_team)+" "+"vs."+" "+Team.get_name(self.away_team)
        elif self.isplayed==True:
          return  Team.get_name(self.home_team)+"("+str(self.score[0])+")"+" "+"vs."+" "+"("+str(self.score[1])+")"+Team.get_name(self.away_team)
    
        
class Season(Match,Team):
    team=[]
    manager=[]
    player=[]
    oyuncuBes=[]
    oyuncuPlayerClass=[]
    def __init__(self,teams, managers, players):
        self.teams=teams
        self.managers=managers
        self.players=players
        self.sayac=0
        try:
            takım=open(self.teams,"r")
            takımOku=takım.readlines()
        except:
            print("Dosyanız Bulunamadı...")
        for i in takımOku:
            Season.team.append(i[:-1])
        try:
            man=open(self.managers,"r")
            manOku=man.readlines()
        except:
            print("Dosyanız Bulunamadı(Manager)")
        for i in manOku:
            Season.manager.append(i[:-1])
        try:
            oyuncu=open(self.players,"r")
            oyuncuOku=oyuncu.readlines()
        except:
            print("Players Dosyanız Bulunamadı...")
        for i in oyuncuOku:
            Season.player.append(i[:-1])
        Season.oyuncuBes=[Season.player[i:i+5] for i in range(0, len(Season.player), 5)]
        self.count=0
        oyuncuİcList=[]
        #for i in range(0,len(Season.team)):
            #ikidenfazla=[]
        for i in Season.oyuncuBes:
            list1=[]
           
            for a in i:
                #print(a)
                if a=="Nando De Colo":
                    b=["Nando De","Colo"]
                    oyuncular=Player(b[0],b[1])
                    Season.oyuncuPlayerClass.append(Player(b[0],b[1]))
                    list1.append(oyuncular)
                else:
                    b=a.split(" ")
                    oyuncular=Player(b[0],b[1])
                    Season.oyuncuPlayerClass.append(Player(b[0],b[1]))
                    list1.append(oyuncular)
                    
        #print(ikidenfazla)
          
            kocİsim=Season.manager[self.count]
            koc=kocİsim.split(" ")
            koc1=Manager(koc[0],koc[1])
            teamName=Season.team[self.count]
            oyuncuİcList.append(Team(teamName,koc1,list1.copy()))
            list1.clear()
            self.count=self.count+1
        random.shuffle(oyuncuİcList)
        self.takımici=oyuncuİcList
        self.fikstür=None
        Season.build_fixture(self)
        self.haf=None
    def build_fixture(self):
        ilkYarıKacHafta=len(Season.team)-1
        sezon=[]
        sezon1=[]
        sözlüklü=[]
        sözlüklüİlkYarı=[]
        sözlüklüİkinciYarı=[]
        count=0
        hafta=1
        haf=18
        sayı=1
        for i in range(ilkYarıKacHafta):
            takımbuild=self.takımici.copy()
            for a in range(0,int((len(self.takımici)/2))):
                a1=random.choice(takımbuild)
                takımbuild.remove(a1)
                a2=random.choice(takımbuild)
                takımbuild.remove(a2)
                l1=[a1,a2]
                l2=[a2,a1]
                if l1.copy() not in sezon:
                    mac1=Match(a1, a2, hafta)
                    sezon.append(mac1)
                    a1.add_to_fixture(a1)
                    a2.add_to_fixture(a2)
                    #a1.takım["fikstür"]={k:a1.takım["fikstür"][k] for k in sorted(a1.takım["fikstür"])}
                    #a2.takım["fikstür"]={k:a2.takım["fikstür"][k] for k in sorted(a2.takım["fikstür"])}
                    sezon1.append(Match(a2, a1, haf))
                    a1.add_to_fixture(a1)
                    a2.add_to_fixture(a2)
                    #a1.takım["fikstür"]={k:a1.takım["fikstür"][k] for k in sorted(a1.takım["fikstür"])}
                    #a2.takım["fikstür"]={k:a2.takım["fikstür"][k] for k in sorted(a2.takım["fikstür"])}
                l1.clear()
                l2.clear()
                
            takımbuild=self.takımici.copy()
            str2=str(haf)+"."+"Hafta"
            str1=str(hafta)+"."+"Hafta"
            sözlüklüİlkYarı.append({str1:sezon.copy()})
            sözlüklüİkinciYarı.append({str2:sezon1.copy()})
            hafta+=1
            haf+=1
            sezon.clear()
            sezon1.clear()
        sözlüklü=sözlüklüİlkYarı+sözlüklüİkinciYarı
        self.fikstür=sözlüklü
    def get_week_fixture(self,week_no):
        hafta=week_no-1
        strİfade= str(hafta+1) +'.Hafta'
        if week_no<1 or week_no>len(self.fikstür):
            return None
        else:
            return self.fikstür[hafta][strİfade]
           
    def get_players(self):
        list1=[]
        for i in self.takımici:
            for c in i.player1:
                list1.append(c)
                    
        return list1
    def get_week_no(self):
        count=0
        haf1=1
        for a in range(len(self.fikstür)):
            for i in self.fikstür[count][str(haf1)+".Hafta"]:
                if i.is_played()==False:
                    self.haf=haf1
                    return haf1
            count+=1
            haf1+=1
    def play_week(self):
        hafta=Season.get_week_no(self)
        count=0
        if hafta==None:
            return None
        else:
            self.sayac+=1
            for i in self.fikstür[hafta-1][str(hafta)+".Hafta"]:
                i.play()
                
    def get_managers(self):
        list1=[]
        for i in self.takımici:
            list1.append(i.manager)
        return list1
    def get_teams(self):
        list2=[]
        for i in self.takımici:
            list2.append(i)
        return list2
    def get_best_player(self):#Burda hata var düzelt
        listem1=[]
        
        """if Season.get_week_no(self)==None:
            haftaSayısı=len(self.fikstür)-1
        else:
            haftaSayısı=int(Season.get_week_no(self))-1"""
        oyuncular=Season.get_players(self)
        if len(oyuncular[0].get_points_detailed())==0:
            return None
        else:
            if Season.get_week_no(self)==None:
                haftaSayısı=len(self.fikstür)-1
            else:
                haftaSayısı=int(Season.get_week_no(self))-1
            listem2=[]
            sözlü=[]
            for i in oyuncular:
                a=i.get_points_detailed()
                #print(a)
                if len(a)==1:
                    a1=a[0]
                elif len(a)==0:
                    continue
                else:
                    a1=a[-1]
                listem2.append(a1)
                b=i
                k=[a1,b]
                söz={"name":b,"point":a1}
                sözlü.append(söz.copy())
                söz.clear()
                listem1.append(k.copy())
                k.clear()
            #print(listem2)
            index=max(listem2)
            liste3=[]
            for i in sözlü:
                if i["point"]==index:
                    liste3.append(i["name"])
            return liste3[0]
    def get_best_manager(self):
        listem1=[]
        koclar=Season.get_managers(self)
        listem2=[]
        sözlü=[]
        d=koclar[0].get_influence_detailed()
        if len(d)==0:
            return None
        for i in koclar:
            a=i.get_influence_detailed()
            if len(a)==1:
                a1=a[0]
            elif len(a)==0:
                continue
            else:
                a1=a[-1]
            listem2.append(a1)
            b=i
            k=[a1,b]
            söz={"name":b,"point":a1}
            sözlü.append(söz.copy())
            söz.clear()
            listem1.append(k.copy())
            k.clear()
        index=max(listem2)
        liste3=[]
        for i in sözlü:
            if i["point"]==index:
                liste3.append(i["name"])
        return liste3[0]
    def get_most_scoring_team(self):
        listem1=[]
        takımlar=Season.get_teams(self)
        listem2=[]
        sözlü=[]
        if len(takımlar[0].takım["points"]["atılan"])==0:
            return None
        for i in takımlar:
            a=i.takım["points"]["atılan"]
            
            if len(a)==1:
                a1=a[0]
                
            elif len(a)==0:
                continue
            else:
                a1=a[-1]
                
            listem2.append(a1)
            b=i
            k=[a1,b]
            söz={"name":b,"point":a1}
            sözlü.append(söz.copy())
            söz.clear()
            listem1.append(k.copy())
            k.clear()
        #print(sözlü)
        index=max(listem2)
        liste3=[]
        #print(index)
        for i in sözlü:
            if i["point"]==index:
                liste3.append(i["name"])
        return liste3[0]
    def get_champion(self): 
        liste=[]
        wins=[]
        if self.sayac==len(self.fikstür):
            for i in self.get_teams():
                a=i.get_wins()
                liste.append([a,i])
                wins.append(a)
            c=max(wins)
            sayac=0
            indeks=[]
            for i in liste:
                if c==i[0]:
                    sayac+=1
                    indeks.append(i[1])
            #print(len(indeks))
            if 1==len(indeks):
                ind=wins.index(c)
                return liste[ind][1]
            elif len(indeks)>1:
                averaj=[]
                bos=[]
                for i in indeks:
                    a=i.get_scored()
                    b=i.get_conceded()
                    c=a-b
                    averaj.append([c,i])
                    bos.append(c)
                kl=max(bos)
                ks=0
                b1=[]
                for i in averaj:
                    if kl==i[0]:
                        ks+=1
                        b1.append(i[1])
                return b1[0]
        else:
            return None
    def reset(self):
        for i in self.get_teams():
            i.reset()
        self.sayac=0
        self.count=0
        Match.isplayed=False
        self.fikstür=None
        self.build_fixture()
    def get_season_length(self):
        takımSayısı=len(self.get_teams())
        sezon=(takımSayısı-1)*2
        return sezon
            
            
            