
from PIL import Image, ImageEnhance, ImageFilter
import os


path = './img'
pathout = './editedImgs'

if not os.path.exists(pathout):
    os.mkdir(pathout)


for fileName in os.listdir(path):

    if fileName.lower().endswith(('.png', '.jpg', '.jpeg')):
        img = Image.open(f"{path}/{fileName}")

    #converting to RGB first
    img = img.convert('RGBA')

    edit = img.filter(ImageFilter.SHARPEN)
    edit =  edit.convert('L')#.rotate(-90)


    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)

    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(fileName)[0]

    edit.save(f"{pathout}/{clean_name}_edited.jpg")