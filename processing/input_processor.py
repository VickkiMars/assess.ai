from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'assess.ai\input_scripts'

class InputProcessError(ValueError):
    """
    Custom exception for errors during input processing
    """
    def __init__(self, message):
        super().__init_(message)

def process_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        raise InputProcessError(f"Error processing text file:\n{e}")

def process_image_file(file_path):
    try:
        image = Image.open(file_path)

        # OCR configurations, tailored for handwriting

        custom_config = '--psm 6'
        text = pytesseract.image_to_string(image, config=custom_config)

        cleaned_text = ''.join(filter(lambda x: x.isprintable(), text))
        return cleaned_text
    except Exception as e:
        raise InputProcessError(f"Error processing image file: \n{e}")

def process_input(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in ['.txt']:
        return process_text_file(file_path)
    elif file_extension.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']:
        return process_image_file(file_path)
    else:
        raise InputProcessError(f"Error processing file: %s" % file_path)
    
if __name__ == "__main__":
    file_path = "file_path_goes_here"
    try:
        content = process_input(file_path)
    except InputProcessError as e:
        print("Input Processing Error: %s" % e)