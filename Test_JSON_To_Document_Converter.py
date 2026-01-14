from JSON_To_Document_Converter import JSON_To_Document_Converter
import os
from pathlib import Path

# SOLID design principles
# Data dumps
# REST API tests
# crash reporting
# runtime errors handling
# Asserts/Error handling

from Timer import Timer 
from Logger import Logger


class Tester:

    def test_JSON_To_Document_Converter(self, input_json_path: str, output_docx_path: str):

        self.remove_file_if_exists(output_docx_path)

        converter = JSON_To_Document_Converter(input_json_path, output_docx_path)
        converter.convert()
        converter.save()

        if self.check_if_file_exists(output_docx_path):
            print("Test passed.")
        else:
            print("Test failed.")

    def remove_file_if_exists(self, path: str):
        file_path = Path(path)
        if file_path.exists():
            file_path.unlink()

    def check_if_file_exists(self, path: str):
        assert os.path.exists(path), "Output DOCX file was not created."

        if not os.path.exists(path):
            return False
        else:
            return True

    def run_tests(self):
        timer = Timer()
        timer.start()
        input_json_paths = ["input.json", "input.json"]
        output_docx_paths = ["output1.docx", "output2.docx"]

        for input_json_path, output_docx_path in zip(input_json_paths, output_docx_paths):    
            timer.start()
            self.test_JSON_To_Document_Converter(input_json_path, output_docx_path)
            print("Time elasped = " + f"{timer.stop():e}")
            print("-----\n")


if __name__ == "__main__":

    tester = Tester()
    tester.run_tests()



