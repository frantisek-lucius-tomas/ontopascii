import math, numpy as np
from PIL import Image, ImageDraw, ImageFont

# characters for the ASCII art
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = np.array(list(chars))
charLength = len(charArray)
interval = charLength / 256

scaleFactor = 0.25

oneCharWidth = 10
oneCharHeight = 14

def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]

# open the image
im = Image.open("images/chameleon.jpg").convert('RGB')

# use a font available on your system
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
# resize image based on the scale factor and character dimensions
im = im.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = np.array(im)

# create an output image
outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

# create an output text file
with open("output.txt", "w") as text_file:
    for i in range(height):
        for j in range(width):
            r, g, b = pix[i, j]
            # convert the RGB value to grayscale using the luminosity formula
            gray = int(0.299*r + 0.587*g + 0.114*b)
            gray = min(255, gray)
            char = getChar(gray)
            
            # write character to text file
            text_file.write(char)
            
            # draw character on the output image
            d.text((j * oneCharWidth, i * oneCharHeight), char, font=fnt, fill=(r, g, b))
        
        text_file.write('\n')

# save the output image
outputImage.save('output/output.png')
