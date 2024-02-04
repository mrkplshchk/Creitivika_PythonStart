

def setup():
    size(1000,1000)
    background(0)
def draw():
    x=random(0,1000)
    y=random(0,1000)
    if mousePressed:# если нажата
        background(0)
    stroke(random(0,255))
    strokeWeight(5)
    point(x,y)
    
    
