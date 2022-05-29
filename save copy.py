from PIL import Image 
images =[ Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/01.jpg"), Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/02.jpg"), Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/03.jpg"), Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/04.jpg")]
x= 0
y=0
ys = []
for i in images:
    tamanho = i.size
    print('img 1 size: ', tamanho) 
    if tamanho[0]> x:
        x = tamanho[0]
    ys.append(y)
    y += tamanho[1]
    
print(x, y, ys)

new_im = Image.new('RGB', (x,y), (250,250,250)) 

for i in range(len(images)):
    new_im.paste(images[i], (0,ys[i])) 
    
new_im.save("merged_images.png", "png") 


import img2pdf 
from PIL import Image 
import os 
img_path = "merged_images.png"
pdf_path = "merged_images.pdf"
image = Image.open(img_path) 
pdf_bytes = img2pdf.convert(image.filename) 
file = open(pdf_path, "wb") 
file.write(pdf_bytes) 
image.close() 
file.close() 
print("Successfully made pdf file") 