import os
from PIL import Image
from fpdf import FPDF

def create_pdf_from_images(folder_path, output_path):
    # Get all image files from the specified folder (in this case, the same folder where the code file is present)
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    pdf = FPDF()

    total_images = len(image_files)
    processed_images = 0

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)

        # Open the image using Pillow
        image = Image.open(image_path)

        # Convert the image to RGB mode (required by FPDF)
        image = image.convert('RGB')

        # Calculate the size of the image to fit it into the PDF page
        pdf_width, pdf_height = pdf.w, pdf.h
        image_width, image_height = image.size
        aspect_ratio = image_width / float(image_height)

        if aspect_ratio >= 1:
            pdf_image_width = pdf_width
            pdf_image_height = pdf_width / aspect_ratio
        else:
            pdf_image_height = pdf_height
            pdf_image_width = pdf_height * aspect_ratio

        # Resize the image to fit the PDF page
        image.thumbnail((pdf_image_width, pdf_image_height))

        # Add a new page to the PDF
        pdf.add_page()

        # Calculate the position to center the image
        x = (pdf_width - image.width) / 2.0
        y = (pdf_height - image.height) / 2.0

        # Add the image to the PDF page
        pdf.image(image_path, x, y, image.width, image.height)

        processed_images += 1

        # Display progress
        progress = processed_images / total_images * 100
        print(f"Processing image {processed_images}/{total_images} - {progress:.2f}%")

    # Save the PDF file
    pdf.output(output_path, 'F')
    print(f"PDF created successfully at: {output_path}")


folder_path = './'
output_path = 'output.pdf'
create_pdf_from_images(folder_path, output_path)
