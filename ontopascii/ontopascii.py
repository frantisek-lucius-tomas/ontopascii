import math, os
from PIL import Image, ImageDraw, ImageFont, ImageSequence

class AsciiSetup:
    # class to convert images and GIFs into ASCII art.

    def __init__(self, scale_factor=0.25, color=True, font_path=None):
        # initializes the AsciiSetup object with the given parameters.
        self.chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]  # characters used for ASCII art, from darkest to lightest.
        self.char_array = list(self.chars)  # converts the characters string to a list.
        self.char_length = len(self.char_array)  # length of the character list.
        self.scale_factor = scale_factor  # scaling factor for output image size.
        self.one_char_width = 10  # width of one ASCII character in pixels.
        self.one_char_height = 14  # height of one ASCII character in pixels.
        self.color = color  # boolean to indicate if the ASCII art should be colored.

        if font_path is None:  # use default font path if none is provided.
            font_path = os.path.join(os.path.dirname(__file__), "fonts", "lucon.ttf")
        
        self.font = ImageFont.truetype(font_path, 15)  # load the font for drawing ASCII characters.

    def get_char(self, value):
        # gets an ASCII character corresponding to a grayscale value.
        return self.char_array[math.floor(value / 256 * self.char_length)]  # maps grayscale value to a character.

    def convert_to_grayscale(self, pixel):
        # converts an RGB pixel to a grayscale value.
        r, g, b = pixel  # extracts the RGB values from the pixel.
        return int(0.299 * r + 0.587 * g + 0.114 * b)  # returns the grayscale value using standard conversion formula.

    def process_frame(self, im):
        # converts a single image frame to ASCII art.
        im = im.resize(
            (
                int(self.scale_factor * im.width),  # resizes width based on scale factor.
                int(self.scale_factor * im.height * (self.one_char_width / self.one_char_height))  # resizes height based on scale factor and character aspect ratio.
            ),
            Image.NEAREST  # uses nearest neighbor resampling.
        )

        output_image = Image.new('RGB', (self.one_char_width * im.width, self.one_char_height * im.height), color=(0, 0, 0))  # creates a new black image to draw ASCII art.
        draw = ImageDraw.Draw(output_image)  # initializes drawing context.

        for i in range(im.height):  # loops through each row of pixels.
            for j in range(im.width):  # loops through each column of pixels.
                pixel = im.getpixel((j, i))  # gets the RGB value of the current pixel.
                grayscale_value = self.convert_to_grayscale(pixel)  # converts the pixel to grayscale.
                ascii_char = self.get_char(grayscale_value)  # gets the corresponding ASCII character.

                if self.color:  # checks if the output should be colored.
                    r, g, b = pixel  # extracts the RGB values from the pixel.
                    enhanced_pixel = (min(int(r * 1.2), 255), min(int(g * 1.2), 255), min(int(b * 1.2), 255))  # enhances the pixel color.
                    draw.text((j * self.one_char_width, i * self.one_char_height), ascii_char, font=self.font, fill=enhanced_pixel)  # draws the ASCII character in color.
                else:
                    draw.text((j * self.one_char_width, i * self.one_char_height), ascii_char, font=self.font, fill=(grayscale_value,) * 3)  # draws the ASCII character in grayscale.

        return output_image  # returns the generated ASCII art image.

    def convert(self, input_path, output_path):
        # converts an image or GIF to ASCII art and saves the result.
        im = Image.open(input_path)  # opens the input image.

        if input_path.lower().endswith('.gif'):  # checks if the input is a GIF.
            output_path += '.gif'  # appends '.gif' to the output path.
            self.process_gif(im, output_path)  # processes the GIF.
        else:
            output_image = self.process_frame(im.convert("RGB"))  # converts a static image to ASCII art.
            output_image.save(output_path + '_image.png')  # saves the result as a PNG file.

    def process_gif(self, im, output_path):
        # processes and converts a GIF to ASCII art, saving it as a new GIF.
        frames = []  # list to store processed frames.

        for frame in ImageSequence.Iterator(im):  # iterates over each frame in the GIF.
            processed_frame = self.process_frame(frame.convert("RGB"))  # converts each frame to ASCII art.
            frames.append(processed_frame)  # adds the processed frame to the list.

        frames[0].save(  # saves the frames as a new GIF.
            output_path, 
            save_all=True, 
            append_images=frames[1:], 
            loop=0, 
            duration=im.info['duration']  # maintains original GIF duration.
        )
