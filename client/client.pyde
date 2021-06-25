add_library('net')

client = []

def setup():
    size(200,200)
    global client
    client = Client(this, "127.0.0.1", 20000)
    
def draw():
    background(100)
    
def mouseClicked():
    s = "(" + str(mouseX) + "," + str(mouseY) + ") was clicked"
    println(s)
    client.write(s)
