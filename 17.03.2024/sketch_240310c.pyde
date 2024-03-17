x=0
y=0
def setup():
    size(1000,1000)
def draw():
    global x,y
    background(0)
    
    if mousePressed:
        ellipse(mouseX,mouseY,200,200)
   
    
