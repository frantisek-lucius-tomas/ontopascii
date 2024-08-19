import os, sys
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure you modify the import path based on your actual project structure
from asciimodule import asciiimage

def test_asciiimage():
    # Paths for test images
    input_image_path = 'input_image.jpg'
    output_image_path = 'test_output_image.png'

    # Create a simple test image
    test_image = Image.new('RGB', (100, 100), color=(255, 0, 0))  # Red image
    test_image.save(input_image_path)

    # Call the asciiimage function
    asciiimage(image_path=input_image_path, output_path=output_image_path, font_size=15, scale_factor=0.25, output_color=1)

    # Verify the output image
    assert os.path.exists(output_image_path), "Output image file does not exist."

    # Check image properties
    output_image = Image.open(output_image_path)
    assert output_image.mode == 'RGB', "Output image is not in RGB mode."
    
    # Verify size (depending on input image size and scaling factor)
    expected_width = int(100 * 10 * 0.25)
    expected_height = int(100 * 14 * 0.25)
    assert output_image.size == (expected_width, expected_height), "Output image size is incorrect."

    # Clean up files
    os.remove(input_image_path)
    os.remove(output_image_path)

    print("All tests passed.")

if __name__ == "__main__":
    test_asciiimage()
