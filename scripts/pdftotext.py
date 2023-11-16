import sys
import pypdf as PyPDF2

def extract_text_from_pdf(input_pdf_path, output_txt_path):
    try:
        with open(input_pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            with open(output_txt_path, 'w', encoding='utf-8') as text_file:
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text_file.write(page.extract_text())

        print(f"Text extracted successfully. Output saved to {output_txt_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py input_pdf output_txt")
    sys.exit(1)

# Get input and output file paths from command line arguments
input_pdf_path = sys.argv[1]
output_txt_path = sys.argv[2]

# Call the function with user-provided input and output paths
extract_text_from_pdf(input_pdf_path, output_txt_path)