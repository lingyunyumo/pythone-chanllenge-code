import urllib, wave, Image
from cStringIO import StringIO
canvas = Image.new('RGB', (300, 300))
url = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav"
for i in range(25):
    wav = wave.open(StringIO(urllib.urlopen(url % (i + 1)).read()))
    piece = Image.fromstring('RGB', (60, 60), wav.readframes(10800))
    canvas.paste(piece, ((i % 5) * 60, (i / 5) * 60))

canvas.show()
