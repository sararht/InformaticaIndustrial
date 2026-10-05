from pathlib import Path
from PyPDF2 import PdfReader

p = Path(r"c:\Users\Sara\Documents\InformaticaIndustrial\temas\control\Programacion-de-Control.pdf")
print('exists', p.exists(), 'size', p.stat().st_size if p.exists() else 0)
reader = PdfReader(str(p))
print('pages', len(reader.pages))
for i, page in enumerate(reader.pages[:12], 1):
    text = (page.extract_text() or '')[:3000]
    print(f'--- PAGE {i} ---\n{text}\n')
