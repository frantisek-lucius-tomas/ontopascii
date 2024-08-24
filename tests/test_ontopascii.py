import unittest
from ontopascii import AsciiArt
import os

class TestAsciiArt(unittest.TestCase):
    def test_image_conversion(self):
        ascii_art = AsciiArt(scale_factor=0.1, color=False)
        input_path = os.path.join(os.path.dirname(__file__), "car.gif")  # Change to .gif if testing GIF
        output_path = os.path.join(os.path.dirname(__file__), "test_output")

        # Ensure the input file exists
        self.assertTrue(os.path.exists(input_path), f"Input file {input_path} does not exist.")

        # Attempt to convert the image
        try:
            ascii_art.convert_image(input_path, output_path)
        except Exception as e:
            self.fail(f"convert_image method raised an exception: {e}")

        # Determine the expected output file extension
        if input_path.lower().endswith('.gif'):
            expected_output = output_path + '.gif'
        else:
            expected_output = output_path + '_image.png'

        # Check if the output file was created
        self.assertTrue(os.path.exists(expected_output), f"Output file {expected_output} was not created.")

if __name__ == '__main__':
    unittest.main()
