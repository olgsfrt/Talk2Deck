import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_file, img_dir):
    # Open the provided PDF file
    doc = fitz.open(pdf_file)

    # Create the directory if it doesn't exist
    os.makedirs(img_dir, exist_ok=True)

    for page_num in range(len(doc)):
        # Get the page
        page = doc.load_page(page_num)

        # Render the page to an image
        pix = page.get_pixmap()

        # Define the output image path
        output_file = f"{img_dir}/page_{page_num + 1}.png"

        # Save the image
        pix.save(output_file)

    print(f"Converted {len(doc)} pages to images and saved in {img_dir}")

