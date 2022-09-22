my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
def generate(row,column):
    listesayı=[]
    
    for i in range(0,row*column):
        listesayı.append(i)
    listesayı=[listesayı[i:i+column] for i in range(0,len(listesayı),column)]
    a=0
    tamliste=[]
    if len(listesayı)==1 or len(listesayı[0])==1:
        return ("The board matrix elements must be between 0:1:row*column-1")
    for i in range(0,len(listesayı)):
        b=listesayı[a]
        tamliste.append(b)
        a=a+1
    return tamliste
def move(board,moves):
    count=0
    moves=moves.lower()
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        for i in moves:
            if i == "d":
                a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                i1=a[0][0] #kaçýncý satýrda
                i2=a[0][1] #kaçýný sütundaü
                a=len(board)-1
                if i1==a:
                    count=count+0
                else:
                    board[i1][i2],board[i1+1][i2]=board[i1+1][i2],board[i1][i2]
                    count=count+1
            elif i== "r":
                    a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                    i1=a[0][0] #kaçıncı satırda
                    i2=a[0][1] #kaçını sütunda
                    a=len(board[0])
                    if int(i2) ==(a-1):
                        count=count+0
                    else:
                        board[i1][i2],board[i1][i2+1]=board[i1][i2+1],board[i1][i2]
                        count=count+1
            elif i=="u":
                a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                i1=a[0][0] #kaçıncı satırda
                i2=a[0][1] #kaçını sütundaü
                if i1==0:
                    count=count+0
                else:
                    board[i1][i2],board[i1-1][i2]=board[i1-1][i2],board[i1][i2]
                    count=count+1
            elif i=="l":
                    a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                    i1=a[0][0] #kaçıncı satırda
                    i2=a[0][1] #kaçını sütunda
                    if int(i2)==0:
                        count=count+0
                    else:
                        board[i1][i2],board[i1][i2-1]=board[i1][i2-1],board[i1][i2]
                        count=count+1
    return count
def get_board_size(board):
    if len(board)==1 or len(board[0])==1:
        return 'The board matrix elements must be between 0:1:row*column-1'
    else:
        return len(board),len(board[0])
def print_board(board):
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            print(board[i][j], end = " ") 
        print() 
def move_right(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
        i1=a[0][0] #kaçıncı satırda
        i2=a[0][1] #kaçını sütunda
        a=len(board[0])
        if int(i2) ==(a-1):
            return 0
        else:
            board[i1][i2],board[i1][i2+1]=board[i1][i2+1],board[i1][i2]
            return 1
def move_left(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
        i1=a[0][0] #kaçıncı satırda
        i2=a[0][1] #kaçını sütunda
        if int(i2)==0:
            return 0
        else:
            board[i1][i2],board[i1][i2-1]=board[i1][i2-1],board[i1][i2]
            return 1
def move_up(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
        i1=a[0][0] #kaçıncı satırda
        i2=a[0][1] #kaçını sütundaü
        if i1==0:
            return 0
        else:
            board[i1][i2],board[i1-1][i2]=board[i1-1][i2],board[i1][i2]
            return 1
def move_down(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
        i1=a[0][0] #kaçıncı satırda
        i2=a[0][1] #kaçını sütundaü
        a=len(board)-1
        if i1==a:
            return 0
        else:
            board[i1][i2],board[i1+1][i2]=board[i1+1][i2],board[i1][i2]
            return 1
def is_valid(board):
    result = sum(board, [])
    result.sort()
    i1=len(board)
    i2=len(board[0])
    listesayı1=[]
    if i1==1 or i2==1:
        return False
    for i in range(0,i1*i2):
        listesayı1.append(i)
    if listesayı1==result:
        return True
    else:
        return False
def reset(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        i1=len(board)
        i2=len(board[0])
        board.clear()
        bos=[]
        for i in range(0,i1*i2):
            bos.append(i)
        bos=[bos[i:i+i2] for i in range(0,len(bos),i2)]
        d=0
        for i in range(0,len(bos)):
            b=bos[d]
            board.append(b)
            d=d+1
        return None
def is_solved(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        i1=len(board)
        i2=len(board[0])
        listesayı1=[]
        
        for i in range(0,i1*i2):
            listesayı1.append(i)
        listesayı1=[listesayı1[i:i+i2] for i in range(0,len(listesayı1),i2)]
        a=0
        tamliste1=[]
        for i in range(0,len(listesayı1)):
            b=listesayı1[a]
            tamliste1.append(b)
            a=a+1
        if listesayı1==board:
            return True
        else:
            return False
def play(board,moves):
    moves=moves.lower()
    count=0
    if is_valid(board)==False:
        return -2
    else:
        if is_solved(board)==True:
            return 0
        else:
            for i in moves:
                if i =="d":
                    b=move_down(board)
                    if b==1:  
                        count=count+1
                        if is_solved(board)==True:
                            return count
                    else:
                        count=count+0
                elif i=="u":
                    c=move_up(board)
                    if c==1:
                        count=count+1
                        if is_solved(board)==True:
                            return count
                    else:
                        count=count+0
                elif i=="r":
                    a=move_right(board)
                    if a==1:
                        count=count+1
                        if is_solved(board)==True:
                            return count
                    else:
                        count=count+0
                elif i=="l":
                    d=move_left(board)
                    if d==1:
                        count=count+1
                        if is_solved(board)==True:
                            return count
                    else:
                        count=count+0
                    
    if is_solved(board)==False:
        return -1
import random
def shuffle(board, times=20):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"

    else:
        ab=times
        islemler=["L","R","D","U"]
        yapılan1=[]
        count=0
        while len(yapılan1)<times:
            yapılan=random.choice(islemler)
            for i in yapılan:
                if i == "D":
                    a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                    i1=a[0][0] #kaçýncý satýrda
                    i2=a[0][1] #kaçýný sütundaü
                    a=len(board)-1
                    if i1==a:
                        ab=ab+1
                    else:
                        board[i1][i2],board[i1+1][i2]=board[i1+1][i2],board[i1][i2]
                        count=count+1
                        yapılan1.append("D")
                elif i== "R":
                        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                        i1=a[0][0] #kaçıncı satırda
                        i2=a[0][1] #kaçını sütunda
                        a=len(board[0])
                        if int(i2) ==(a-1):
                            ab=ab+1
                        else:
                            board[i1][i2],board[i1][i2+1]=board[i1][i2+1],board[i1][i2]
                            yapılan1.append("R")
                elif i=="U":
                    a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                    i1=a[0][0] #kaçıncı satırda
                    i2=a[0][1] #kaçını sütundaü
                    if i1==0:
                        ab=ab+1
                    else:
                        board[i1][i2],board[i1-1][i2]=board[i1-1][i2],board[i1][i2]
                        yapılan1.append("U")
                elif i=="L":
                        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                        i1=a[0][0] #kaçıncı satırda
                        i2=a[0][1] #kaçını sütunda
                        if int(i2)==0:
                            ab=ab+1
                        else:
                            board[i1][i2],board[i1][i2-1]=board[i1][i2-1],board[i1][i2]
                            yapılan1.append("L")
        i1=len(board)
        i2=len(board[0])
        listesayı1=[]
        
        for i in range(0,i1*i2):
            listesayı1.append(i)
        listesayı1=[listesayı1[i:i+i2] for i in range(0,len(listesayı1),i2)]
        a=0
        tamliste1=[]
        for i in range(0,len(listesayı1)):
            b=listesayı1[a]
            tamliste1.append(b)
            a=a+1
        if tamliste1!=board:
            return yapılan1
        else:
            return shuffle(board,times)                        
                    
def rotate(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        newboard=list(zip(*board))           
        newboard1=[l[::-1] for l in newboard]
        newboard1 = [list(ele) for ele in newboard1]
        return newboard1
def move_random(board):
    if len(board)==1 or len(board[0])==1:
        return "The board matrix elements must be between 0:1:row*column-1"
    else:
        islemler=["L","R","D","U"]
        yapılan1=[]
        ab=0
        count=0
        while len(yapılan1)<1:
            yapılan=random.choice(islemler)
            for i in yapılan:
                if i == "D":
                    a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                    i1=a[0][0] #kaçýncý satýrda
                    i2=a[0][1] #kaçýný sütundaü
                    a=len(board)-1
                    if i1==a:
                        ab=ab+1
                    else:
                        board[i1][i2],board[i1+1][i2]=board[i1+1][i2],board[i1][i2]
                        count=count+1
                        yapılan1.append("D")
                elif i== "R":
                        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                        i1=a[0][0] #kaçıncı satırda
                        i2=a[0][1] #kaçını sütunda
                        a=len(board[0])
                        if int(i2) ==(a-1):
                            ab=ab+1
                        else:
                            board[i1][i2],board[i1][i2+1]=board[i1][i2+1],board[i1][i2]
                            yapılan1.append("R")
                elif i=="U":
                    a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                    i1=a[0][0] #kaçıncı satırda
                    i2=a[0][1] #kaçını sütundaü
                    if i1==0:
                        ab=ab+1
                    else:
                        board[i1][i2],board[i1-1][i2]=board[i1-1][i2],board[i1][i2]
                        yapılan1.append("U")
                elif i=="L":
                        a=[(i, board.index(0)) for i, board in enumerate(board) if 0 in board]
                        i1=a[0][0] #kaçıncı satırda
                        i2=a[0][1] #kaçını sütunda
                        if int(i2)==0:
                            ab=ab+1
                        else:
                            board[i1][i2],board[i1][i2-1]=board[i1][i2-1],board[i1][i2]
                            yapılan1.append("L")
        return yapılan1
def play_interactive(board=None):
    if board==None:
        print("Please type the puzzle size number.")
        row=int(input(" Row number:"))
        column= int(input(" Column number:"))
        a1=generate(row,column)
        a2=shuffle(a1,times=20)
        print(a2)
        board=a1
        print(board)
        print(is_valid(board))
        if is_valid(board)==True:
            sayı=0
            hareketler=[]
            print(is_solved(board))
            if is_solved(board)==False:
                while is_solved(board)==False:
                    print("Current board is:")
                    print_board(board)
                    hareket=input("Where do you want to move: ")
                    hareket1=hareket.lower()
                    if len(hareket1)==1:
                        if hareket1 in ("q","d","u","l","r","m"):
                            if hareket1=="m":
                                a=move_random(board)
                                sayı=sayı+1
                                hareketler.append(a[0].lower())
                            elif hareket1=="d":
                                b1=move_down(board)
                                if b1==1:
                                    sayı=sayı+1
                                    hareketler.append("d")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="u":
                                b2=move_up(board)
                                if b2==1:
                                    sayı=sayı+1
                                    hareketler.append("u")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="r":
                                b3=move_right(board)
                                if b3==1:
                                    sayı=sayı+1
                                    hareketler.append("r")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="l":
                                b4=move_left(board)
                                if b4==1:
                                    sayı=sayı+1
                                    hareketler.append("l")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="q":
                                print("Exiting.")
                                return (hareketler,-1)
                                break
                        else:
                            print("Wrong Move.")
                    elif(len(hareket1))!=1:
                        print("Wrong Move.")
                if is_solved(board)==True:
                    print_board(board)
                    print("Congrats! You solved the board in "+ str(sayı)+" moves.")

                    return (hareketler,sayı)
                else:
                    return (hareketler,-1)
        else:
            if is_valid(board)==False:
                print("The board matrix elements must be between 0:1:row*column-1")
                return ('',-2)
    else:
        sayı=0
        hareketler=[]
        if is_valid(board)==True:
            if is_solved(board)==False:
                while is_solved(board)==False:
                    print("Current board is:")
                    print_board(board)
                    hareket=input("Where do you want to move: ")
                    hareket1=hareket.lower()
                    if len(hareket1)==1:
                        if hareket1 in ("q","d","u","l","r","m"):
                            if hareket1=="m":
                                a=move_random(board)
                                hareketler.append(a[0].lower())
                                sayı=sayı+1
                            elif hareket1=="d":
                                b1=move_down(board)
                                if b1==1:
                                    sayı=sayı+1
                                    hareketler.append("d")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="u":
                                b2=move_up(board)
                                if b2==1:
                                    sayı=sayı+1
                                    hareketler.append("u")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="r":
                                b3=move_right(board)
                                if b3==1:
                                    sayı=sayı+1
                                    hareketler.append("r")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="l":
                                b4=move_left(board)
                                if b4==1:
                                    sayı=sayı+1
                                    hareketler.append("l")
                                else:
                                    sayı=sayı+0
                            elif hareket1=="q":
                                print("Exiting.")
                                return (hareketler,-1)
                                break
                        else:
                            print("Wrong Move.")
                    elif len(hareket1)!=0:
                        print("Wrong Move.")
                if is_solved(board)==True:
                    print_board(board)
                    print("Congrats! You solved the board in "+ str(sayı)+" moves.")
                    return (hareketler,sayı)
                else:
                    return (hareketler,-1)
        else:
            if is_valid(board)==False:
                print("The board matrix elements must be between 0:1:row*column-1")
                return ('',-2)
        
            
                            
                    
                
                
                    
                    
                    
                    
                    