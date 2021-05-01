from graphicsLibrary import *

class Screen():
    #Creates a binary matrix
    def __init__(self,hight,width):
        self.array=matrix(hight,width,0)
        self.hight=hight
        self.width=width
    def __del__(self):
        pass
    def print(self,matrixWin,tkWin):
        for m in range(self.hight):
            for n in range(self.width):
                if self.array[n][m]==0:
                    matrixWin.array[n][m]=Label(tkWin,text=".",bg='black',fg='black')
                    matrixWin.array[n][m].pack(padx=m,pady=n)
                elif self.array[n][m]==1:
                    matrixWin.array[n][m]=Label(tkWin,text=".",bg='black',fg='white')
                    matrixWin.array[n][m].pack(padx=m,pady=n)

class Window():
    def winInit(self,n,m,window,bgColor):
        #Creates a labels matrix of n x m
        matrix=[]
        for i in range(n):
            a=[]
            for j in range(m):
                a.append(Label(window,text=".",bg=bgColor,fg=bgColor))
                a[j].pack(padx=j,pady=i)
            matrix.append(a)
        return matrix
    def __init__(self,n,m,window,bgColor,fgColor):
        self.n=n
        self.m=m
        self.bgColor=bgColor
        self.fgColor=fgColor
        self.array=self.winInit(n,m,window,bgColor)

class Player(Point):
    #Creates a point
    def __init__(self,x,y,username):
        Point.__init__(self,x,y)
        self.username=username
#A simple point is p<number id>. A player is p0<number id>.