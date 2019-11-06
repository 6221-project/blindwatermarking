import cv2
import re
import os
#from catalog import image_tool as it

# Create your tests here.

#img = it.load_image('C:\OneDrive\GWU\CSCI6221\Project\TestImage.JPG')
#print(img.shape)

path = r"C:\Users\79109\gm\workplace\BlindWaterMarking-python\blindwatermarking\catalog\media\bwm_original_image.jpg"
#h = re.findall(r'(?:[A-Z]:|\\|(?:\.{1,2}[\/\\])+)[\w+\\\s_\(\)\/]+(?:\.\w+)*', path)
h = re.findall(r"(.+\\).+?\.", path)
print(h)

# join two
def join_path(*args):
    s = ''
    for v in args:
        s = os.path.join(s, v)
    return s

h = join_path('abc','pwd','aaa')
print(h)


