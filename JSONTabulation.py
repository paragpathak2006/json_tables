import json
from docx import Document

class JSONTabulator:

    def tabulate(self, container: Document, data):

        if not isinstance(data, (dict, list)):
            container.add_paragraph(str(data))
            return

        # Excel table
        if self.is_arr(data):
            self.excel_table(container, data)
            return

        # Dictionary table
        if isinstance(data, dict):
            table = container.add_table(rows=len(data), cols=2)
            table.style = "Table Grid"

            for r, (k, v) in enumerate(data.items()):
                key_cell = table.cell(r, 0)
                val_cell = table.cell(r, 1)

                key_cell.text = str(k)
                val_cell.text = ""

                if isinstance(v, (dict, list)):
                    self.tabulate(val_cell, v)
                else:
                    val_cell.text = "" if v is None else str(v)

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

    def excel_table(self,container, array):

        # All columns 
        columns = []
        for obj in array:
            for k in obj.keys():
                if k not in columns:
                    columns.append(k)

        table = container.add_table(rows=len(array) + 1, cols=len(columns))
        table.style = "Table Grid"

        # First row
        for c, col in enumerate(columns):
            cell = table.cell(0, c)
            cell.text = col

        # Data rows
        for r, obj in enumerate(array, start=1):
            for c, col in enumerate(columns):
                cell = table.cell(r, c)
                cell.text = ""

                value = obj.get(col)
                if isinstance(value, (dict, list)):
                    self.tabulate(cell, value)
                else:
                    cell.text = "" if value is None else str(value)

    # checks if input is array of objects
    def is_arr(self, arr):
        return (
            isinstance(arr, list)
            and arr
            and all(isinstance(x, dict) for x in arr)
        )


    pass
