import json
from docx import Document
from html2docx import html2docx


"""
For html 
"""
def add_html(container, html):
    temp_doc = Document(html2docx(html, title=""))

    for p in temp_doc.paragraphs:
        target_p = container.add_paragraph()
        for run in p.runs:
            r = target_p.add_run(run.text)
            r.bold = run.bold
            r.italic = run.italic
            r.underline = run.underline

"""
The main recursive tabulation class 
"""
class JSONTabulator:

    def tabulate(self, container: Document, data):

        if not isinstance(data, (dict, list)):
            # container.add_paragraph(str(data))
            add_html(container, str(data))
            return

        #   Excel-style table for array of objects
        if self.is_arr(data):
            self.excel_table(container, data)
            return

        # Dictionary style table for objects and arrays
        if isinstance(data, dict):
            table = container.add_table(rows=len(data), cols=2)
            table.style = "Table Grid"

            for row, (k, v) in enumerate(data.items()):
                key = table.cell(row, 0)
                value = table.cell(row, 1)

                key.text = str(k)
                value.text = ""

                if isinstance(v, (dict, list)):
                    self.tabulate(value, v)
                else:
                    value.text = "" if v is None else str(v)

            return

        if isinstance(data, list):
            table = container.add_table(rows=len(data), cols=1)
            table.style = "Table Grid"

            for i, item in enumerate(data):
                cell = table.cell(i, 0)
                cell.text = ""
                if isinstance(item, (dict, list)):
                    self.tabulate(cell, item)
                else:
                    cell.text = str(item)

    """ Excel-style table for array of objects """
    def excel_table(self,container, array):

        # All columns 
        columns = []
        for obj in array:
            for key in obj.keys():
                if key not in columns:
                    columns.append(key)

        table = container.add_table(rows=len(array) + 1, cols=len(columns))
        table.style = "Table Grid"

        # First row
        for colum, col in enumerate(columns):
            cell = table.cell(0, colum)
            cell.text = col

        # Data rows
        for row, obj in enumerate(array, start=1):
            for colum, col in enumerate(columns):
                cell = table.cell(row, colum)
                cell.text = ""

                value = obj.get(col)
                if isinstance(value, (dict, list)):
                    self.tabulate(cell, value)
                else:
                    cell.text = "" if value is None else str(value)

    """checks if input is array of objects"""
    def is_arr(self, arr):
        return (
            isinstance(arr, list)
            and arr
            and all(isinstance(x, dict) for x in arr)
        )


    pass
