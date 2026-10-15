"""
Career Copilot AI - Sample Resume Generator
Creates a valid sample .docx resume file using standard library zipfile and XML.
"""

import os
import zipfile

def create_sample_docx(output_path: str):
    """Generate a clean Word .docx document containing an authentic engineering resume."""
    doc_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        <w:p><w:r><w:t>Alex Mercer</w:t></w:r></w:p>
        <w:p><w:r><w:t>Email: alex.mercer@example.com | Phone: (555) 019-2834</w:t></w:r></w:p>
        <w:p><w:r><w:t>GitHub: github.com/alexmercer | LinkedIn: linkedin.com/in/alexmercer</w:t></w:r></w:p>

        <w:p><w:r><w:t>PROFESSIONAL SUMMARY</w:t></w:r></w:p>
        <w:p><w:r><w:t>Machine Learning Engineer with hands-on experience developing deep learning models, retrieval-augmented generation pipelines, and containerized FastAPI services. Proven track record in model optimization and low-latency inference.</w:t></w:r></w:p>

        <w:p><w:r><w:t>TECHNICAL SKILLS</w:t></w:r></w:p>
        <w:p><w:r><w:t>Languages: Python, SQL, C++, Bash</w:t></w:r></w:p>
        <w:p><w:r><w:t>Frameworks: PyTorch, Scikit-Learn, Hugging Face, FastAPI, LangChain</w:t></w:r></w:p>
        <w:p><w:r><w:t>Tools &amp; Platforms: Docker, Git, Linux, PostgreSQL, Redis, ChromaDB, MLflow</w:t></w:r></w:p>

        <w:p><w:r><w:t>WORK EXPERIENCE</w:t></w:r></w:p>
        <w:p><w:r><w:t>Machine Learning Engineering Intern | TechNova Solutions (June 2025 - Present)</w:t></w:r></w:p>
        <w:p><w:r><w:t>• Engineered customer churn prediction model in Scikit-Learn, boosting validation PR-AUC by 18%.</w:t></w:r></w:p>
        <w:p><w:r><w:t>• Packaged model into asynchronous FastAPI microservice, achieving sub-30ms p95 latency under simulated load.</w:t></w:r></w:p>
        <w:p><w:r><w:t>• Developed automated data validation checks reducing ETL ingestion errors by 40%.</w:t></w:r></w:p>

        <w:p><w:r><w:t>KEY PROJECTS</w:t></w:r></w:p>
        <w:p><w:r><w:t>Production RAG Document Assistant (Python, PyTorch, ChromaDB, FastAPI)</w:t></w:r></w:p>
        <w:p><w:r><w:t>• Implemented hybrid search combining BM25 keyword matching and dense embeddings with Reciprocal Rank Fusion.</w:t></w:r></w:p>
        <w:p><w:r><w:t>• Applied Cross-Encoder reranking to filter top 20 retrieved candidates to top 4 with verifiable citations.</w:t></w:r></w:p>
        <w:p><w:r><w:t>• Built multi-stage Docker container with automated regression testing in GitHub Actions.</w:t></w:r></w:p>

        <w:p><w:r><w:t>EDUCATION</w:t></w:r></w:p>
        <w:p><w:r><w:t>B.S. in Computer Science | State Engineering University (Graduated May 2025)</w:t></w:r></w:p>
        <w:p><w:r><w:t>Relevant Coursework: Machine Learning, Algorithms &amp; Data Structures, Database Systems, Linear Algebra</w:t></w:r></w:p>

        <w:p><w:r><w:t>CERTIFICATIONS</w:t></w:r></w:p>
        <w:p><w:r><w:t>DeepLearning.AI Machine Learning Specialization | AWS Certified Cloud Practitioner</w:t></w:r></w:p>
    </w:body>
</w:document>
"""

    content_types_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

    rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types_xml)
        z.writestr("_rels/.rels", rels_xml)
        z.writestr("word/document.xml", doc_xml)
    print(f"Sample DOCX created at {output_path}")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    docx_file = os.path.join(out_dir, "sample_engineering_resume.docx")
    create_sample_docx(docx_file)

