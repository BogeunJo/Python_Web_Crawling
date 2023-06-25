import numpy
from PIL import Image
import os

target = 'C:\\Users\\lg\\Desktop\\파일자동화\\새 폴더'

if not os.path.exists(target):
    os.mkdir(target)

for i in range(0,101):
    filename=f'image{i}.jpg'

    rgb_array= numpy.random.rand(720, 1080, 3)*255

    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

    image.save(os.path.join(target, filename))

