# Image_to_Pdf Automation

Image_to_Pdf Automation is a Python script that streamlines the process of converting a folder containing image files (PNG, JPG, JPEG) into a single PDF file. The script automates this task by utilizing the Python Imaging Library (PIL) and the FPDF library, making it a quick and efficient solution for converting multiple images into a well-organized PDF document.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)
- FPDF library

Before running the script, ensure you have the necessary libraries installed. You can install them using the following pip commands:

```bash
pip install pillow
pip install fpdf
```

## Usage

1. Download the script `Image_to_Pdf.py` from this repository.

2. Place the script in the directory containing the images you want to convert to PDF.

3. Double-click on the `Image_to_Pdf.py` script. The script will automatically process the images in the folder and generate a PDF file named `output.pdf`, containing all the images.

## Supported Image Formats

The script supports the following image formats:

- PNG (Portable Network Graphics)
- JPG (Joint Photographic Experts Group)
- JPEG (Joint Photographic Experts Group)

We can also include other image formats by adding their extensions to the `image_files` list in the script.

## Notes

- The script is designed to center the images on the PDF pages, creating a visually appealing PDF document.

- During image processing, the script will display progress as a percentage of completed images.

## Acknowledgments

- The script utilizes the powerful Pillow library for image processing.

- It also relies on the efficient FPDF library to generate the final PDF output.

---
