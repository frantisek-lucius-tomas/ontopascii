import math
from PIL import Image, ImageDraw, ImageFont

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

# scale this number for better rendering
scaleFactor = 0.2

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]

text_file = open("output.txt", "w")

# place here your image here that you want in ascii
im = Image.open("here.png").convert('RGB')

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        h = min(255, h)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j * oneCharWidth, i * oneCharHeight), getChar(h), font=fnt, fill=(r, g, b))

    text_file.write('\n')

text_file.close()

outputImage.save('output.png')
