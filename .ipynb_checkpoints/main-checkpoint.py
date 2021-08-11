import os
import tempfile
from pdf2image import convert_from_bytes
 
filename = '/home/darix/Documents/python/recognitve_paragraphe_image_digital/data/pdf/simple_a.pdf'
 
images = convert_from_bytes(open('data/pdf/simple.pdf', 'rb').read())
 
base_filename  =  os.path.splitext(os.path.basename(filename))[0] 
print(base_filename)    
 
save_dir = '/home/darix/Documents/python/recognitve_paragraphe_image_digital/data/image/'
 
for page,i in zip(images,range(len(images)+1)):
    page.save(os.path.join(save_dir, base_filename+str(i)+'.jpg'), 'JPEG')
