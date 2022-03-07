#AAA up, TTT down, CCC left, GGG right
from cmath import atan
import random

bloblist=[]
for n in range (1,1001):
    blob=""
    for i in range (0,5):
        blob+=random.choice(["A","T","C","G"])
    bloblist.append(blob)

print(bloblist)


class Blob:
    def __init__(self, gene):
        for blob in bloblist:
            self.gene=blob
            self.dy = gene.count('T') - gene.count('A')
            self.dx = gene.count('G') - gene.count('C')
            self.x = random.random()
            self.y = random.random()
            self.x+=self.dx
            self.y+=self.dy


    
