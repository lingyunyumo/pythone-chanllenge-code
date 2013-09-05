import Image
n = 100
im = Image.new('RGB', (n, n))
wire = Image.open('wire.png')
count = 0
for x in range(n*2):
    y = x//4
    first = y+1
    last = n-y
    if x%4 == 0:
        first -= 1
    if x%4 == 3:
        last -= 1
    for i in range(first, last):
        im.putpixel((i, y), wire.getpixel((count+i-first, 0)))        
    im = im.rotate(90)
    count += last - first
im.show()

