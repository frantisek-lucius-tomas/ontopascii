import math
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageSequence

# ASCII characters arranged from darkest to lightest
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
char_array = list(chars)
char_length = len(char_array)
scale_factor = 0.25

one_char_width = 10
one_char_height = 14

# Set to 1 for colored output, 0 for grayscale output
color = 1

# Function to map pixel intensity to an ASCII character
def get_char(value):
    return char_array[math.floor(value / 256 * char_length)]

# Function to convert a pixel to grayscale using a weighted sum
def convert_to_grayscale(pixel):
    r, g, b = pixel
    return int(0.299 * r + 0.587 * g + 0.114 * b)

def process_frame(im):
    # Resize the image for ASCII conversion
    im = im.resize(
        (int(scale_factor * im.width), int(scale_factor * im.height * (one_char_width / one_char_height))),
        Image.NEAREST
    )

    # Create the output image
    output_image = Image.new('RGB', (one_char_width * im.width, one_char_height * im.height), color=(0, 0, 0))
    draw = ImageDraw.Draw(output_image)

    for i in range(im.height):
        for j in range(im.width):
            pixel = im.getpixel((j, i))
            grayscale_value = convert_to_grayscale(pixel)
            ascii_char = get_char(grayscale_value)

            if color == 1:
                r, g, b = pixel
                enhanced_pixel = (min(int(r * 1.2), 255), min(int(g * 1.2), 255), min(int(b * 1.2), 255))
                draw.text((j * one_char_width, i * one_char_height), ascii_char, font=font, fill=enhanced_pixel)
            else:
                draw.text((j * one_char_width, i * one_char_height), ascii_char, font=font, fill=(grayscale_value,) * 3)

    return output_image

def process_gif(input_path, output_path):
    # Open the GIF file
    im = Image.open(input_path)
    
    # Create a list to hold all the processed frames
    frames = []
    
    for frame in ImageSequence.Iterator(im):
        processed_frame = process_frame(frame.convert("RGB"))
        frames.append(processed_frame)

    # Save the frames as a new GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=im.info['duration'])

# Set the font for the output image
font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

# Path to the input file
input_path = "car.jpg"  # Change to your file
output_path = "output_ascii"

# Determine the file type and process accordingly
if input_path.lower().endswith('.gif'):
    output_path += '.gif'
    process_gif(input_path, output_path)
else:
    # Process as a single image
    im = Image.open(input_path)
    output_image = process_frame(im.convert("RGB"))
    output_image.save(output_path + '_image.png')
