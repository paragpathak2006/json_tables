import os
from time import time
import unittest
from Timer import Timer
from JSON_To_Document_Converter import JSON_To_Document_Converter
from DOCXComparator import DOCXComparator

class Run_Unit_Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        print("\nSetting up JSON to DOCX conversion test...\n")

        cls.benchmark_file_path = "benchmark.docx"
        cls.input_file_paths = ["input.json", "input.json"]
        cls.output_file_paths = ["output1.docx", "output2.docx"]
        cls.times = ["0.1", "0.1"]
        cls.maxTimeAllowed = 0.2  # Example time limit of 5 seconds

        for output_file_path in cls.output_file_paths:
            if os.path.exists(output_file_path):
                os.remove(output_file_path)

        timer = Timer()
        i = 0
        for input_json_path, output_docx_path, time in zip(cls.input_file_paths, cls.output_file_paths, cls.times):
            timer.start()
            converter = JSON_To_Document_Converter(input_json_path, output_docx_path)
            converter.convert()
            converter.save()

            cls.times[i] = f"{timer.stop():0.2e}"
            print("input_json_path =", input_json_path)
            print("output_docx_path =", output_docx_path)
            print("time =", cls.times[i])
            print(f"Conversion time for {input_json_path} to {output_docx_path} = " + cls.times[i])
            print("-----\n\n")
            i += 1

    def test_docx_file_created(self):
        print("\n\n1. checking if docx files were created...")
        for output_file_path in self.output_file_paths:
            self.assertTrue(os.path.exists(output_file_path),"Output DOCX file was not created: " + output_file_path)
        print("Test OK\n\n")


    def test_docx_file_xml_with_benchmark(self):
        print("\n\n2. comparing docx file xml with benchmark...")        
        for output_file_path in self.output_file_paths:
            self.assertTrue(DOCXComparator.compare_document_xml(output_file_path, self.benchmark_file_path),"Failed XML comparison for " + output_file_path)
        print("Test OK\n\n")

    def test_docx_file_text_and_tables_with_benchmark(self):
        print("\n\n3. comparing docx file text and tables with benchmark...")    
        for output_file_path in self.output_file_paths:
            self.assertTrue(DOCXComparator.compare_text_and_tables(output_file_path, self.benchmark_file_path),"Failed text and table comparison for " + output_file_path)
        print("Test OK\n\n")

    def test_docx_performance(self):
        print("\n\n4. checking performance times...")
        for time in self.times:
            self.assertTrue(float(time) < self.maxTimeAllowed, f"Time {time} exceeded the allowed time in {self.maxTimeAllowed:.2e}")  # time limit failed  

        print("Test OK\n\n")


if __name__ == "__main__":
    unittest.main()
