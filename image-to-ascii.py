import math, numpy as np
from PIL import Image, ImageDraw, ImageFont

# ascii characters from dark to light, reversed to map grayscale correctly
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = np.array(list(chars))
charLength = len(charArray)
interval = charLength / 256

scaleFactor = 0.25

# scale for characters
oneCharWidth = 10
oneCharHeight = 14

outputColor = 1 # 1 for colored image 0 for blackandwhites

# mapping a grayscale intensity value
def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]

# load image and convert to RGB
image = Image.open("images/chameleon.jpg").convert('RGB')

# set up font
fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

# resize image
width, height = image.size
image = image.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))), Image.NEAREST)
width, height = image.size
pix = np.array(image)

# create a new image for the output
outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

# process the image and generate ASCII art
with open("output.txt", "w") as text_file:
    for i in range(height):
        for j in range(width):
            r, g, b = pix[i, j]
            
            # convert to grayscale
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray = min(255, gray)
            char = getChar(gray)
            
            # write the character to the text file
            text_file.write(char)
            
            # determine the fill color based on blackAndWhite flag
            if outputColor == 1:
                fillColor = (r, g, b)
            else:
                fillColor = (gray, gray, gray)

            # draw the character on the output image
            d.text((j * oneCharWidth, i * oneCharHeight), char, font=fnt, fill=fillColor)
        
        text_file.write('\n')

# save the output image
outputImage.save('output/output.png')
