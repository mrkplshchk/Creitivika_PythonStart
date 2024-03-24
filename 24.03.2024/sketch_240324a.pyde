def collideCircleCircle(x, y,d, x2, y2, d2):

    if dist(x,y,x2,y2) <= (d/2)+(d2/2):
        return True
    else:
        return False


def setup():
    size(600, 400)
    
def draw():
    background(100)
    if collideCircleCircle(300, 200, 50, mouseX, mouseY, 100):
        fill(255, 0, 0)
    else:
        fill(255)
    ellipse(300, 200, 50, 50)
    ellipse(mouseX, mouseY, 100, 100)
