img=0
mode="вправо"
x=0
def setup():
    global img
    size(1000,1000)
    img=loadImage("e.jpg")
def draw():
    global img,mode,x
    background(0)
    image (img,x,100,450,650)
    if (mode == "вправо") and mousePressed:
        x=x+10
    if (mode == "влево") and mousePressed:
        x=x-10
    if x <=0:
        mode = "вправо"
    if x>=600:
        mode = "влево"
    
        
    
    
    
    
    
    
    
    
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
