import Image
im = Image.open('mozart.gif')
imX, imY = im.size
data = list(im.getdata())
newIm = Image.new("RGB", (imX, imY))
finalData = []
for y in range(imY):
    myData = data[imX*y:(imX*(y+1))]
    pos = myData.index(195) # 195 is pink in palette
    finalData.extend(myData[pos:])
    finalData.extend(myData[:pos])
newIm.putdata(finalData)
newIm.show()
