from PIL import Image 

img_01 = Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/01.jpg") 
img_02 = Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/02.jpg") 
img_03 = Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/03.jpg") 
img_04 = Image.open("mangas/omniscient-reader-s-viewpoint/capitulo-04/04.jpg") 
  
img_01_size = img_01.size 
img_02_size = img_02.size 
img_03_size = img_02.size 
img_02_size = img_02.size 
  
print('img 1 size: ', img_01_size) 
print('img 2 size: ', img_02_size) 
print('img 3 size: ', img_03_size) 
print('img 4 size: ', img_03_size) 
  
new_im = Image.new('RGB', (img_01_size[0],2*img_01_size[1]), (250,250,250)) 
  
new_im.paste(img_01, (0,0)) 
new_im.paste(img_03, (0,img_01_size[1])) 
  
new_im.save("merged_images.png", "PNG") 
new_im.show()