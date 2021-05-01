from tkinter import *

def matrix(n,m,value):
  #Creates a void matrix of n x m
  matriz = []
  for i in range(n):
    a = [value]*m
    matriz.append(a)
  return matriz

class Point():
  #Creates a point
  def __init__(self,x,y):
    self.x=x
    self.y=y
    self.vx=0
    self.vy=0
  def __del__(self):
    pass
  def move(self,i,j):
    self.x+=i
    self.y+=j
    self.vx=i
    self.vy=j
  def refresh(self,screen,window):
    screen.print(window)
    i=self.x
    j=self.y
    vi=self.vx
    vj=self.vy
    screen.array[(j-vj)%screen.width][(i-vi)%screen.hight]=0
    screen.array[j%screen.width][i%screen.hight]=1

class Line():
  #Creates a line
  def __init__(self,p1,p2):
    self.p1=p1
    self.p2=p2
  def __del__(self):
    pass
  def move(self,i1,j1,i2,j2):
    self.p1.move(i1,j1)
    self.p2.move(i2,j2)
  def paramX(self,t):
    return t*self.p1.x+(1-t)*self.p2.x
  def paramY(self,t):
    return t*self.p1.y+(1-t)*self.p2.y
  def refresh(self,screen,window):
    screen.print(window)
    for k in range(11):
      t=k/10
      i=int(round(self.paramX(t)))
      j=int(round(self.paramY(t)))
      screen.array[j-1][i-1]=1