from pypdf import PdfReader
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# When running locally, this file is in `backend/` and data lives in `../data`.
# In Lambda, both `resources.py` and `data/` are placed at the zip root (`/var/task/...`).
DATA_DIR = os.path.join(BASE_DIR, "data")
if not os.path.exists(DATA_DIR):
    DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))


def data_path(filename: str) -> str:
    return os.path.join(DATA_DIR, filename)

# Read LinkedIn PDF
try:
    reader = PdfReader(data_path("linkedin.pdf"))
    linkedin = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            linkedin += text
except FileNotFoundError:
    linkedin = "LinkedIn profile not available"

# Read other data files
with open(data_path("summary.txt"), "r", encoding="utf-8") as f:
    summary = f.read()

with open(data_path("style.txt"), "r", encoding="utf-8") as f:
    style = f.read()

with open(data_path("facts.json"), "r", encoding="utf-8") as f:
    facts = json.load(f)