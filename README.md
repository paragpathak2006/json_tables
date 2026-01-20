# JSON to DOCX tabulator

### **Input** : JSON file
Input is a simple JSON file

### **Output** : DOCX file
Output consists of a DOCX file with a tabulated JSON

### **Dependencies**
```bash
pip install html4docx python-docx
```

### **Run**
To run copy and paste the following

```bash
python -m unittest run_unit_tests.py
```

# JSON To Document Converter
This is the main wrapper class that handles the full operation. A JSON file is directly converted to DOCX file by this class. Internally three objects handle the three parts of the operation Import, Process and export.

```mermaid
graph LR;
    X(JSON To Document Converter) --> A(JSON Importer);
    X --> B(JSON Tabulation);
    X --> C(Document Exporter);
    style X fill:#111111,stroke:#333,stroke-width:4px
    style A fill:red,stroke:#333,stroke-width:4px
    style B fill:green,color:#fff
    style C fill:red,stroke:#333,stroke-width:4px
```

Code follows the following flow

```mermaid
graph LR;
    S[.json] --> A(JSON Importer)

    A --> B(JSON Tabulation);
    B --> C(Document Exporter);
    C --> D[.docx];

    style B fill:green,color:#fff
    style A fill:red,stroke:#333,stroke-width:4px
    style C fill:red,stroke:#333,stroke-width:4px
    style S fill:#111111,stroke:#333,stroke-width:4px
    style D fill:#111111,stroke:#333,stroke-width:4px
```

### JSON Importer
This class is resposible for importing the JSON file

### JSON Tabulation
This class is resposible for processing the JSON data and converting it into a document

### Document Exporter
This class is resposible exporting the data into the file document.

