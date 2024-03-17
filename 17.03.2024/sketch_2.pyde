img=0
def setup():
    global img
    size(1000,1000)
    img=loadImage("r.jpg")
def draw():
    global img
    translate(0)
    image(img,0,0)
    fill(255,0,0)
    ellipse(200,800,150,150)
    ellipse(400,800,150,150)
    ellipse(600,800,150,150)
    ellipse(800,800,150,150)
    fill(0,0,0)
    text(u'вниз',200,800)
    text(u'вверх',400,800)
    text(u'вправо',600,800)
    text(u'влево',800,800)
def mouseClicked():
    global img
     #если круглая кнопка нажата
    xDif = 200 - mouseX
    yDif = 800 - mouseY
    
    if sqrt(xDif*xDif + yDif*yDif) < 75:
        
