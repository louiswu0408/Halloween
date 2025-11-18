import math #import math
import random  #import random
import pygame  #import pygame
pygame.init()

RED = (255, 0, 0) #set color:red
YELLOW=(255,204,0)   #set color:yellow
Myellow=(254,252,215)  #set color:Moon yello
PURPLE=(138, 104, 255)  #set color:purple
purple=(51,0,102) #set color:dark purple
BLUE=(0,0,255) #set color:blue
BLACK=(0,0,0) #set color:black
GREEN = (0,255,0) #set color:green
ORANGE=(255,105,30) #set color:orange
WHITE=(240,255,240) #set color:white
SIZE = (1000, 700) #set the size
screen = pygame.display.set_mode(SIZE) # set the size of the image
def li(a,b,c,d,e): #define a function to draw lines
    pygame.draw.line(screen,BLACK,(a,b),(c,d),e) # draw a "e" width black line from (a,b) to (c,d)

def tri(a,b,c,d,e,f): #define a function to draw a triangle 
    pygame.draw.polygon(screen,BLACK,((a,b),(c,d),(e,f)))  #draw a black triangle that the vertexs are(a,b),(c,d),(e,f)

pygame.draw.rect(screen,PURPLE,(0,0,1000,700))#to turn the color of background to purple
pygame.draw.circle(screen,Myellow,(500,350),280)# to draw the mooon
pygame.draw.rect(screen,purple,(0,630,1000,70))# to draw the bot part of the image to be dark purple 

def star():#define a function to draw stars
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)#draw a lot of stars
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)
    pygame.draw.circle(screen,WHITE,(random.randint(0,1000),random.randint(0,300)),3)#draw a lot of stars
star()# run the function to draw a lot of stars
star()
star()
star()
star()
star()
star()
star()
star()
star()
star()
star()# draw a lot of stars

li(130,630,170,400,40)#to draw the tree
li(170,400,110,380,20)
li(110,380,50,300,20)
li(50,300,40,270,10)
li(100,370,115,340,20)
li(115,340,135,320,20)
li(135,320,134,300,10)
li(158,400,175,330,40)
li(170,400,196,390,40)
li(196,390,210,370,40)
li(175,340,195,230,35)
li(195,230,205,190,30)
li(205,190,215,165,20)
li(215,165,220,160,15)
li(220,160,225,150,10)
tri(190,310,190,360,215,295)
tri(200,260,190,300,235,245)#to draw the tree


pygame.draw.rect(screen,BLACK,(200,400,400,230))#draw the house
tri(150,630,260,630,185,350)
tri(200,400,250,320,405,345)
tri(380,380,500,380,465,255)
tri(450,380,620,380,525,255)
tri(465,255,500,380,525,255)
pygame.draw.rect(screen,BLACK,(400,380,200,20))
pygame.draw.rect(screen,BLACK,(475,230,40,30))#draw the house

pygame.draw.rect(screen,YELLOW,(200,450,200,100))#windows
tri(280,450,290,550,290,450)
pygame.draw.rect(screen,BLACK,(290,450,40,100))
pygame.draw.rect(screen,BLACK,(200,450,40,100))
tri(240,450,240,550,255,550)
tri(200,400,405,400,405,345)
pygame.draw.circle(screen,YELLOW,(495,350),30)
pygame.draw.rect(screen,YELLOW,(470,450,20,100))
pygame.draw.rect(screen,YELLOW,(500,450,20,100))
li(465,350,525,350,7)
li(495,380,495,320,7)
li(247,500,430,500,10)
li(260,450,270,550,7)
li(360,450,370,550,7)#windows
def yrect(a,b,c,d):#define a fuction to draw rectangle
    pygame.draw.rect(screen,YELLOW,(a,b,c,d))# draw a "c"width, "d" height yello rectangle that the left top point is(a,b)
yrect(470,560,50,10)#draw the steps of the house
yrect(465,570,50,10)
yrect(460,580,50,10)
yrect(455,590,50,10)
yrect(450,600,50,10)
yrect(445,610,50,10)#draw the steps of the house 

pygame.draw.line(screen,PURPLE,(230,630),(200,400),2)#draw a line to devide the tree and the house 

pygame.draw.rect(screen,BLACK,(600,450,150,180))# draw the right part of the house
tri(750,450,750,520,795,520)
tri(750,630,750,520,770,520)
yrect(630,535,115,60)
tri(745,535,745,595,730,595)
tri(630,535,630,595,635,595)
li(630,570,740,570,10)
li(690,535,690,595,8)

r1=random.randint(50,950)# set r1 a random number between 50 to 950
r2=random.randint(600,677)# set r2 a random number between 600 to 677(make sure the pupkin won't be too high)
r3=random.randint(50,950)#set r3 a random number between 50 to 950
r4=random.randint(600,677)# set r4 a random number between 600 to 677(make sure the pupkin won't be too high)
def pum(a,b):#define a function to draw pumpkins
    pygame.draw.circle(screen,ORANGE,(a,b),20)#draw a circle
    pygame.draw.ellipse(screen,ORANGE,(a-5,b-23,40,46))#draw a ellipse
    pygame.draw.circle(screen,ORANGE,(a+30,b),20)#draw a circle
    pygame.draw.arc(screen,GREEN, (a+10, b-35, 30, 25), math.pi/2  , math.pi,10)#draw a arc
pum(r1,r2)#set a random locaton for pumpkin
pum(r3,r4)#set a random locaton for pumpkin

r5=random.randint(30,970)#ser r5 a random number between 30 and 970
r6=random.randint(40,660)#ser r6 a random number between 40 and 660
r7=random.randint(30,970)#ser r7 a random number between 30 and 970
r8=random.randint(40,660)#ser r8 a random number between 40 and 660
def gh(a,b):#defien a function to draw a ghost
    pygame.draw.circle(screen,WHITE,(a,b),30)
    pygame.draw.rect(screen,WHITE,(a-30,b,60,40))
    pygame.draw.circle(screen,BLACK,(a-10,b),5)
    pygame.draw.circle(screen,BLACK,(a+10,b),5)
    pygame.draw.arc(screen,WHITE, (a-30,b+34,12,12),math.pi,0,12)
    pygame.draw.arc(screen,PURPLE,(a-18,b+34,12,12),0,math.pi,12)
    pygame.draw.arc(screen,WHITE, (a-6,b+34,12,12),math.pi,0,12)
    pygame.draw.arc(screen,PURPLE,(a+6,b+34,12,12),0,math.pi,12)
    pygame.draw.arc(screen,WHITE, (a+18,b+34,12,12),math.pi,0,12)
gh(r5,r6)#set a random location for ghost
gh(r7,r8)#set a random location for ghost
pygame.display.flip()
pygame.time.wait(30000000)#set the time for displaying
pygame.quit()#stop displaying