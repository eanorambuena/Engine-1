#Imports resources

from tkinter import *
from graphicsLibrary import *
from engineLibrary import *

#Sets params
name="Mi juego"
n=480
m=720
bgColor='black'
fgColor='white'
'''
#Tkinter setup
tkinterW=Tk()
tkinterW.title(name)
tkinterW.geometry(str(m)+"x"+str(n))
tkinterW.configure(background=bgColor)
'''
#Engine setup
matrixW=Window(n,m,tkinterW,bgColor,fgColor)
s1=Screen(n,m)
p01=Player(0,1,"John")

#Graphics setup
p1=Point(1,2)
p2=Point(5,3)
l=Line(p1,p2)

#Game loop
c=0
while c<1000:
    #Tkinter setup
    tkinterW=Tk()
    tkinterW.title(name)
    tkinterW.geometry(str(m)+"x"+str(n))
    tkinterW.configure(background=bgColor)
    if c%100==0:
        p01.refresh(s1,matrixW)
        l.refresh(s1,matrixW)
        s1.print(matrixW)
        p01.move(1,1)
    c+=1
    tkinterW.mainloop()

