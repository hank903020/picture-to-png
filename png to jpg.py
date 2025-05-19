import os
from PIL import Image


def read_directory(directory_name):
    # this loop is for read each image in this foder,directory_name is the foder name with images.
    i = 1
    for filename in os.listdir(directory_name):
        # print(filename)
        im = Image.open(directory_name+'\\'+filename)
        if im.mode == 'P':
            im = im.convert('RGB')
        i = str(i)  # change to str
        im.save(directory_name+'\\'+i+'.jpg')
        i = int(i)  # change to int
        i = i+1


file = input('filename(D:\\\\.....):')
read_directory(file)
# 轉換JPG
'''
im = Image.open('D:\\game\\gall\\mega\\足\\aimai_pet\\001.png')
im.save('D:\\game\\gall\\mega\\足\\aimai_pet\\001jpg.jpg')
'''
