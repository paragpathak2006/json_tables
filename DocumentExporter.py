from docx import Document

""" Document Exporter Class """
class DOCXExporter:
    def __init__(self, output_path: str):

        assert output_path.endswith(".docx"), "Output file must have a .docx extension."

        self.file_path = output_path
        self.document = Document()

    def save(self):
        self.document.save(self.file_path)