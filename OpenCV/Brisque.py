import imquality.brisque as brisque
import PIL.Image

path = r'path'
img = PIL.Image.open(path)
print(brisque.score(img))


#from pdf2image import convert_from_path
#pages = convert_from_path(path, 500)

#for page in pages:
#    page.save(r'path', 'JPEG')


#from PIL import Image, ImageDraw, ImageFilter

#im1 = Image.open(r'path1')
#im2 = Image.open(r'path2')
#back_im = im1.copy()
#back_im.paste(im2, (400, 100))
#back_im.save(r'path1', quality=95)
import os
import imquality.brisque as brisque
import PIL.Image
source_Imgs_folder = 'srcfolder'
scores={}
for filename in os.listdir(source_Imgs_folder):
    if filename.endswith(".jpg"):
        source_file = os.path.join(source_Imgs_folder, filename)
        img = PIL.Image.open(source_file)
        score = brisque.score(img)
        scores[filename] = score
print(scores)



import pandas as pd
import statistics as stats
df = pd.DataFrame.from_dict(scores, orient='index', columns=['score'])
print(df)



print(stats.mean(df['score']))
