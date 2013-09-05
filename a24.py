from Image import open

maze = open("maze.png")
dest = (1,640)
(x,y) = (639,1)
stack = []
def tryMove(dx,dy):
    return (maze.getpixel((x+dx, y+dy))[2] == 0 and (x+dx, y+dy, 0))
 
while (x,y) != dest:
    maze.putpixel((x,y), (maze.getpixel((x,y))[0], 0, 255, 255))
    stack.append((x,y, maze.getpixel((x,y))[0]) )
    x,y,tmp = tryMove(-1,0) or tryMove(1,0) or tryMove(0,1) or tryMove(0,-1) or (stack.pop() and stack.pop())
print(stack[:100]) 
file("maze.zip", "wb").write("".join(map(lambda (x, y, r): chr(r), filter(lambda (x,y,r): (x^y)&1==0, stack))));
