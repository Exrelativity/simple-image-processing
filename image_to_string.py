import pytesseract
from PIL import Image
import argparse

def process_image(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image, config='--psm 11')

    return text

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Process an image to extract text using pytesseract")

    # Add an argument for the image path
    parser.add_argument("image_path", help="Path to the image file")

    # Parse the command line arguments
    args = parser.parse_args()

    # Process the image
    result = process_image(args.image_path)

    # Print the extracted text
    print("Extracted Text:")
    print(result)

if __name__ == "__main__":
    main()
