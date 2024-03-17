bg=0
t=0
def setup():
    size(1000,1000)
def draw():
    global bg,t
    background(0)
    ellipse(bg,t,350,350)
def mouseClicked():
    global bg,t
     #если круглая кнопка нажата
    xDif = bg - mouseX
    yDif = t - mouseY
    
    if sqrt(xDif*xDif + yDif*yDif) < 175:
        bg=random(1000)
        t=random(1000)
