import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageSequence

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\\\|()1{}[]?-_+~<>i!lI;:,\"^`\'. "[::-1]
charArray = np.array(list(chars))
charLength = len(charArray)
interval = charLength / 256

scaleFactor = 0.25

oneCharWidth = 10
oneCharHeight = 14

def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]

def frame_to_ascii(image):
    image = image.convert('RGB')
    width, height = image.size
    image = image.resize((int(scaleFactor * width), int(scaleFactor * height * (oneCharWidth / oneCharHeight))), Image.NEAREST)
    width, height = image.size
    pix = np.array(image)

    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[i, j]

            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray = min(255, gray)
            char = getChar(gray)

            d.text((j * oneCharWidth, i * oneCharHeight), char, font=fnt, fill=(r, g, b))
    
    return outputImage

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

input_gif_path = 'input.gif'
output_gif_path = 'output.gif'

gif = Image.open(input_gif_path)
frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

ascii_frames = [frame_to_ascii(frame) for frame in frames]

ascii_frames[0].save(output_gif_path, save_all=True, append_images=ascii_frames[1:], loop=0, duration=gif.info['duration'])
