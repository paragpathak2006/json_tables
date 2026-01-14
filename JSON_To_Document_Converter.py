from JSONImporter import JSONImporter
from JSONTabulation import JSONTabulator
from DocumentExporter import DocumentExporter

from docx import Document
""" JSON to Document Converter Class """
class JSON_To_Document_Converter:
    def __init__(self, input_path_json: str, output_path_docx: str):

        self.importer = JSONImporter(input_path_json)
        self.exporter = DocumentExporter(output_path_docx)

        self.tabulator = JSONTabulator()

    def convert(self):
        self.tabulator.tabulate(self.exporter.document, self.importer.data)

    def save(self):
        self.exporter.save()