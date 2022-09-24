from django.utils.timezone import now


media = [
    ("Documento pdf", "Questo è un documento pdf", "demo_data/read.pdf", True, now()),
    ("Documento word", "Questo è un documento word", "demo_data/readthedoc.docx", False, now()),
    ("Documento excel", "Questo è un documento excel", "demo_data/calculus.xlsx", False, now()),
]
