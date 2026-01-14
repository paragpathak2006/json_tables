import json
import os

""" JSON Importer Class """
class JSONImporter:
    def __init__(self, file_path: str):

        assert os.path.getsize(file_path) > 0, f"Input file '{file_path}' is empty."
        assert file_path.endswith(".json"), "Input file must have a .json extension."
        assert os.path.exists(file_path), f"Input file '{file_path}' does not exist."
        assert os.path.isfile(file_path), f"Input path '{file_path}' is not a file."
        assert os.access(file_path, os.R_OK), f"Input file '{file_path}' is not readable."

        with open(file_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        assert self.data, "JSON data is empty."
        assert isinstance(self.data, (dict, list)), "JSON root must be an object or an array."
    


