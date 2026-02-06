import os

from utils.pdf_extractor import extract_text_from_pdf
from ocr.ocr_engine import extract_text_from_image


SUPPORTED_IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]


def ingest_document(file_path: str) -> str:
    """
    Detects document type and extracts text accordingly.
    Supports PDF and image files.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)

    elif ext in SUPPORTED_IMAGE_EXTENSIONS:
        return extract_text_from_image(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")
