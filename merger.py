import os
from PyPDF2 import PdfFileMerger
path = "pdfs/omniscient-reader-s-viewpoint/capitulo-03"
x = [str(f'{path}/{a}') for a in os.listdir(path) if a.endswith(".pdf")]
merger = PdfFileMerger()
for pdf in x:
    merger.append(open(pdf, 'rb'))
with open(f"{path}/{path.split('/')[-1]}.pdf", "wb") as fout:
    merger.write(fout)
