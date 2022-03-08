gene="ATACG"
a=0
b=0
c=0
for letters in gene:
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
    a=a/5
    b=b/5
    c=c/5 
    colorcode=(a,b,c)
    return(colorcode)