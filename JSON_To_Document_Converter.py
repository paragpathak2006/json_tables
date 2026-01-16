from JSONImporter import JSONImporter
from JSONTabulation import JSONTabulator
from DocumentExporter import DOCXExporter

from docx import Document
""" JSON to Document Converter Class """
class JSON_To_Document_Converter:
    def __init__(self, input_path_json: str, output_path_docx: str):

        assert isinstance(input_path_json, str), "input_path_json must be a string."
        assert isinstance(output_path_docx, str), "output_path_docx must be a string"
        assert input_path_json.endswith('.json'), "input_path_json must be a JSON file."
        assert output_path_docx.endswith('.docx'), "output_path_docx must be a DOCX file."

        self.importer = JSONImporter(input_path_json)
        self.exporter = DOCXExporter(output_path_docx)
        self.tabulator = JSONTabulator(self.exporter.document, self.importer.data)

    def convert(self):
        self.tabulator.convert()

    def save(self):
        self.exporter.save()