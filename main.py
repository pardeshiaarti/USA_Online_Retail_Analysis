# Convert the uploaded Jupyter Notebook to a Python script

import nbformat
from nbconvert import PythonExporter

# Paths
notebook_path = "/mnt/data/USA_Online_Store_Transaction_Analysis.ipynb"
output_path = "/mnt/data/USA_Online_Store_Transaction_Analysis.py"

# Read the notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

# Convert to Python script
exporter = PythonExporter()
python_script, _ = exporter.from_notebook_node(notebook)

# Save the .py file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(python_script)

output_path
