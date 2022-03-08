#A up, T down, C left, G right
import random
from sys import exit
from webbrowser import get
import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution")
clock=pygame.time.Clock()

        
bloblist=[]
for n in range (1,1001):
    blob=""
    for i in range (0,4):
        blob+=random.choice(["A","T","C","G"])
    bloblist.append(blob)
blobcor=[]
for genes in bloblist:
    x = random.randint(0,500)
    y = random.randint(0,500)
    a=0
    b=0
    c=0
    for letters in genes:
        if letters=="A": ##more blue, goes up
            a +=0
            b +=255
            c +=255
        if letters=="T": ##more green, goes down
            a +=0
            b +=255
            c +=0
        if letters=="C": ##more yellow, goes left
            a += 255
            b +=255
            c +=0
        if letters=="G": #more magenta, goes right
            a += 255
            b+=0
            c+=255
        a=int(a/4)
        b=int(b/4)
        c=int(c/4) 
        colorcode=(a,b,c)
    blobcor.append([x,y,colorcode,genes])


blobpic=pygame.Surface((5,5))
def get_final_position(): ##in 125 steps, where the blobs will end up
    finalposition=[]
    while True:
        for t in range(1,126):
            a=0
            screen.fill((0,0,0))
            ##define the savespace:
            xs=100
            ys=100
            safezone=pygame.Surface((xs,ys))
            safezone.fill((173,255,47))    
            screen.blit(safezone,(0,0))
            while a<1000:
                dy = bloblist[a].count('T') - bloblist[a].count('A')
                dx = bloblist[a].count('G') - bloblist[a].count('C')
                x=blobcor[a][0]
                y=blobcor[a][1]
                blobcor[a][0]=x+dx
                blobcor[a][1]=y+dy
                blobpic.fill(blobcor[a][2])    
                screen.blit(blobpic,(x,y))
                if t==125:
                    finalposition.append([blobcor[a][0],blobcor[a][1],blobcor[a][3]])
                a+=1   
            pygame.display.update()
            clock.tick(60)
            a=0
            t+=1  
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        

# get_final_position()

# newgenlist=[]
# for ind in range(0,1000):
#     if finalposition[ind][0]<=xs and finalposition[ind][1]<=ys:
#         newgenlist.append(finalposition[ind][2])
#         newgenlist.append(finalposition[ind][2])
#         ##those who made it to the safe zone get to reproduce twice

# print(newgenlist)