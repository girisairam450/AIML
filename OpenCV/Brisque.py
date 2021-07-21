# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:09:41 2020

@author: girisairam.ragam
"""

import imquality.brisque as brisque
import PIL.Image

path = r'D:\girisairam.ragam\My Downloads\KYC Images\Uid_3082873.jpg'
img = PIL.Image.open(path)
print(brisque.score(img))


#from pdf2image import convert_from_path
#pages = convert_from_path(path, 500)

#for page in pages:
#    page.save(r'C:\Users\girisairam.ragam\Desktop\IQBotPractise\2COATSANDPACK.jpg', 'JPEG')


#from PIL import Image, ImageDraw, ImageFilter

#im1 = Image.open(r'C:\Users\girisairam.ragam\Desktop\aadhar\aadhar.jpg')
#im2 = Image.open(r'C:\Users\girisairam.ragam\Desktop\aadhar\capture.jpg')
#back_im = im1.copy()
#back_im.paste(im2, (400, 100))
#back_im.save(r'C:\Users\girisairam.ragam\Desktop\aadhar\new.jpg', quality=95)
import os
import imquality.brisque as brisque
import PIL.Image
source_Imgs_folder = 'C:/Users/girisairam.ragam/Desktop/aadhar/Source/'
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