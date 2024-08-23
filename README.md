# asciiart

The ASCIIART library is a Python tool for converting images into ASCII art. It uses the Python Imaging Library (PIL) to process images and transform them into ASCII representations based on grayscale intensity values.

## Features
 - Convert images to ASCII art.
 - Support for color and grayscale ASCII art.
 - Customizable scale factor for resizing images.
 - Optional font customization for ASCII characters.
 - Supports both static images and animated GIFs.

## Installation
1. Install the required dependencies using pip:
    pip install pillow

2. Ensure you have the lucon.ttf font file in the fonts directory or specify a path to your preferred font file.

## Usage

### Convert Static Images

from asciiart import AsciiArt

Initialize the AsciiArt object
ascii_art = AsciiArt(scale_factor=0.1, color=False)

Convert an image to ASCII art
ascii_art.convert_image('path/to/your/image.jpg', 'output_image')

For colored ASCII art
ascii_art.convert_image('path/to/your/image.jpg', 'output_image', color=True)

### Convert GIFs

from asciiart import AsciiArt

Initialize the AsciiArt object
ascii_art = AsciiArt(scale_factor=0.1, color=False)

Convert a GIF to ASCII art
ascii_art.convert_gif('path/to/your/animation.gif', 'output_gif')

For colored ASCII art GIFs
ascii_art.convert_gif('path/to/your/animation.gif', 'output_gif', color=True)

autor name : frantisek tomas
