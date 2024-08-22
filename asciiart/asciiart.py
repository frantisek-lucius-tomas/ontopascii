import math, os
from PIL import Image, ImageDraw, ImageFont, ImageSequence

class AsciiArt:
    def __init__(self, scale_factor=0.25, color=True, font_path=None):
        self.chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
        self.char_array = list(self.chars)
        self.char_length = len(self.char_array)
        self.scale_factor = scale_factor
        self.one_char_width = 10
        self.one_char_height = 14
        self.color = color

        if font_path is None:
            font_path = os.path.join(os.path.dirname(__file__), "fonts", "lucon.ttf")
        self.font = ImageFont.truetype(font_path, 15)

    def get_char(self, value):
        return self.char_array[math.floor(value / 256 * self.char_length)]

    def convert_to_grayscale(self, pixel):
        r, g, b = pixel
        return int(0.299 * r + 0.587 * g + 0.114 * b)

    def process_frame(self, im):
        im = im.resize(
            (int(self.scale_factor * im.width), int(self.scale_factor * im.height * (self.one_char_width / self.one_char_height))),
            Image.NEAREST
        )

        output_image = Image.new('RGB', (self.one_char_width * im.width, self.one_char_height * im.height), color=(0, 0, 0))
        draw = ImageDraw.Draw(output_image)

        for i in range(im.height):
            for j in range(im.width):
                pixel = im.getpixel((j, i))
                grayscale_value = self.convert_to_grayscale(pixel)
                ascii_char = self.get_char(grayscale_value)

                if self.color:
                    r, g, b = pixel
                    enhanced_pixel = (min(int(r * 1.2), 255), min(int(g * 1.2), 255), min(int(b * 1.2), 255))
                    draw.text((j * self.one_char_width, i * self.one_char_height), ascii_char, font=self.font, fill=enhanced_pixel)
                else:
                    draw.text((j * self.one_char_width, i * self.one_char_height), ascii_char, font=self.font, fill=(grayscale_value,) * 3)

        return output_image

    def convert_image(self, input_path, output_path):
        im = Image.open(input_path)
        if input_path.lower().endswith('.gif'):
            output_path += '.gif'
            self.process_gif(im, output_path)
        else:
            output_image = self.process_frame(im.convert("RGB"))
            output_image.save(output_path + '_image.png')

    def process_gif(self, im, output_path):
        frames = []
        for frame in ImageSequence.Iterator(im):
            processed_frame = self.process_frame(frame.convert("RGB"))
            frames.append(processed_frame)

        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=im.info['duration'])
