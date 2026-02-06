from utils.document_ingestor import ingest_document

text = ingest_document("data/uploaded_docs/sample.pdf")
print(text[:500])
