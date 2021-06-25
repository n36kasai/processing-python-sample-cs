add_library('net')

server = []


def setup():
    size(600, 600)
    global server
    server = Server(this, 20000) 

def draw():
    
    global server
    c = server.available()
    if c is not None:
        s = c.readString()
        println("server received: " + s)
        server.write(s)

    background(100)

    
