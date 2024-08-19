import math, numpy as np
from PIL import Image, ImageDraw, ImageFont

# ASCII characters sorted by intensity (darkest to lightest)
CHARACTERS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."[::-1]
CHAR_ARRAY = np.array(list(CHARACTERS))
CHAR_LENGTH = len(CHAR_ARRAY)
INTERVAL = CHAR_LENGTH / 256  # interval to map grayscale values to characters

# map a grayscale intensity value to an ASCII character
def get_char(input_int):
    return CHAR_ARRAY[math.floor(input_int * INTERVAL)]

# main function to convert an image to ASCII art
def asciiimage(image_path, output_path, font_size=15, scale_factor=0.25, output_color=1):

    # load the image and convert to RGB format
    image = Image.open(image_path).convert('RGB')
    width, height = image.size

    # set the width and height of each ASCII character
    # these values ensure dense and detailed ASCII art
    one_char_width = 10
    one_char_height = 14

    # resize the image to match the character dimensions
    image = image.resize(
        (int(scale_factor * width), 
         int(scale_factor * height * (one_char_width / one_char_height))), 
        Image.NEAREST
    )
    width, height = image.size
    pix = np.array(image)

    # load the chosen font (hardcoded path)
    font_path = 'fonts/lucon.ttf'  # hardcoded font path
    font = ImageFont.truetype(font_path, font_size)

    # create a new blank image for the ASCII art output
    output_image = Image.new('RGB', (one_char_width * width, one_char_height * height), color=(0, 0, 0))
    draw = ImageDraw.Draw(output_image)

    # generate the ASCII art by mapping each pixel to an ASCII character
    for i in range(height):
        for j in range(width):
            r, g, b = pix[i, j]  # get the RGB values of the pixel
            gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)  # convert to grayscale
            pixel_char = get_char(gray)  # map grayscale to ASCII character
            
            # draw the ASCII character on the output image
            if output_color:
                draw.text((j * one_char_width, i * one_char_height), pixel_char, font=font, fill=(r, g, b))
            else:
                draw.text((j * one_char_width, i * one_char_height), pixel_char, font=font, fill=(gray, gray, gray))

    # save the final ASCII art image
    output_image.save(output_path)

# example usage
asciiimage(image_path='input_image.jpg', output_path='output_image.png')
