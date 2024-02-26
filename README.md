# Image to String Conversion App

This simple command-line app uses pytesseract to process an image and extract text.

## Prerequisites

Make sure you have the following installed on your system:

- Tesseract OCR: [Install Tesseract](https://github.com/tesseract-ocr/tesseract)

Install the required Python packages:

```bash
pip install pytesseract Pillow
```

## Usage

### Clone the repository

```bash
git clone https://github.com/Exrelativity/simple-image-processing.git
cd simple-image-processing
```

### Run the app

```bash
python image_to_string.py path/to/your/image.png

#e.g 
python3.10 image_to_string.py we_love_live_music_template_with_text_mask_poster-1.jpg
```

### result

<img src="Screen Shot 2024-02-26 at 09.20.52.png">

The image read
<img src="we_love_live_music_template_with_text_mask_poster-1.jpg">
