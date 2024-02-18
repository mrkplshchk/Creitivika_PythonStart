img=0
x=0
f=0
def setup():
    global img,x,f
    size(1000,1000)
    img=loadImage("1.png")
def draw():
    global img,x,f
    if mousePressed:
        background(255,0,0)
        x=x+4
    else:
        background(0,255,0)
    push()
    translate(500,500)
    imageMode(CENTER)
    rotate(radians(x))
    image(img,0,0,650,650)
    x=x+0
    pop()
    fill(0,0,0)
    f = loadFont("ComicSansMS-48.vlw")# настраиваем шрифт (название шрифта, размер, True)
    textFont(f) # включаем шрифт f
    # text(u'С 23 февраля!', 300,150) # печатаем текст (текст, x, y)
    text('S 23 Fevralya!', 300,150) # печатаем текст (текст, x, y)
