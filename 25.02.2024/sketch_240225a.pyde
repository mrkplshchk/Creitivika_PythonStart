u=0
x=0
def setup():
    size(1000,1000)
def draw():
    global x,u
    textSize(30)
    push()
    stroke(u)
    strokeWeight(x)
    if mousePressed:
        noStroke()
    line(mouseX,mouseY,mouseX,mouseY)
    print(mouseX)
    pop()
    fill(255,255,255)
    rect(350,700,200,200)
    fill(0,255,0)
    rect(600,700,200,200)
    fill(0,0,255)
    rect(100,700,200,200) # button
    fill(0)
    text(u"размер",150,800)
    text(u"стерание",400,800)
    text(u"цвет",700,800)
def mouseClicked():
    global x,u
    # кнопка размер
    if mouseX > 100 and mouseX < 300 and mouseY > 700 and mouseY < 900:
        x=x+4
    if mouseX > 600 and mouseX < 800 and mouseY > 700 and mouseY < 900:
        u=255
    if mouseX > 350 and mouseX < 550 and mouseY > 700 and mouseY < 900:
        background(0)
