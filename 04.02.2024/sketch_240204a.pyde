x=0
mode="влево"
def setup():
    size(1000,1000)
def draw():
    global x,mode
    background(0)
    ellipse(x,500,350,350)
    if mode == "вправо":
        x = x + 1
    if mode == "влево":
        x = x - 1
    print(x)
    if mousePressed and (mouseButton==LEFT):# если нажато
        mode="влево"
    if mousePressed and (mouseButton==RIGHT):# иначе (если не нажато)
        mode="вправо"
    
    
