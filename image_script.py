from girls.models import Girl, ModelImage

from os import listdir
from os.path import isfile, join, isdir

mypath = 'media/images'


folders = [f for f in listdir(mypath)]

print(folders)

for folder in folders:
    if 'Check' not in folder:
        path = join(mypath, folder)

        if isdir(path):

            for p in listdir(path):
                pic = join(path, p)
                print(folder)
                pic = pic.replace('media/', '')
                print("PIC", pic)
                g = Girl.objects.filter(image_id=folder).first()
                image = ModelImage(image=pic, model_id=g.id)
                image.save()





