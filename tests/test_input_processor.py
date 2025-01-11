import unittest
from unittest.mock import patch, mock_open, MagicMock
from input_processor import process_text_file, process_image_file, process_input, InputProcessError
from PIL import Image

class TestInputProcessor(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="This is a sample text")
    def test_process_text_file(self, mock_file):
        # Test processing a valid text file
        file_path = "assess.ai\tests\assets\sample.txt"
        content = process_text_file(file_path)
        self.assertEqual(content, "This is a sample text.")
        mock_file.assert_called_with(file_path, 'r', encoding='utf-8')

    @patch("input_processor.Image.open")
    @patch("input_processor.pytesseract.image_to_string", return_value="Handwritten text extracted.")
    def test_process_image_file(self, mock_ocr, mock_image_open):
        # Test processing a valid image file
        file_path = "assess.ai\tests\assets\handwritten.png"
        content = process_image_file(file_path)
        self.assertEqual(content, "Handwritten text extracted")
        mock_image_open.assert_called_once_with(file_path)
        mock_ocr.assert_called_once()

    def test_process_text_file_error(self):
        # Tests that InputProcessError is raised when a text file is missing or inaccessible
        with self.assertRaises(InputProcessError) as context:
            process_text_file("non_existent.txt")
        self.assertIn("Error processing text file", str(context.exception))

    @patch("input_processor.Image.open", side_effect=FileNotFoundError("Image file not found"))
    def test_process_image_file_error(self, mock_image_open):
        # Tests that InputProcessError is raised when an image file is missing or inaccessible
        with self.assertRaises(InputProcessError) as context:
            process_image_file("non_existent.png")
        self.assertIn("Error processing image file", str(context.exception))
    
    @patch("builtins.open", new_callable=mock_open, read_data="This is a sample text.")
    def test_process_input_text_file(self, mock_file):
        # Tests that "process_input" correctly delegates to "process_text_file" method for text files
        file_path = "assess.ai\tests\assets\document.txt"
        content = process_input(file_path)
        self.assertEqual(content, "This is a sample text.")
        mock_file.assert_called_with(file_path, 'r', encoding='utf-8')

    @patch("input_processor.Image.open")
    @patch("input_processor.pytesseract.image_to_string", return_value="Extracted Image text.")
    def test_process_input_image_file(self, mock_ocr, mock_image_open):
        # Tests that "process_input" correctly delegates to "process_text_file" method for text files
        file_path = "assess.ai\tests\assets\image.png"
        content = process_input(file_path)
        self.assertEqual(content, "Extracted Image text.")
        mock_image_open.assert_called_once_with(file_path)
        mock_ocr.assert_called_once()

    def test_process_input_unsupported__file(self):
        # Test process_input with an unsupported file type
        file_path = "unsupported_file.xyz"
        with self.assertRaises(InputProcessError) as context:
            process_input(file_path)
        self.assertIn("Unsupported file type", str(context.exception))

if __name__ == "__main__":
    unittest.main()

# To run: python -m unittest test_input_processor.py