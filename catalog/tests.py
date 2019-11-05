import cv2
import re
#from catalog import image_tool as it

# Create your tests here.

#img = it.load_image('C:\OneDrive\GWU\CSCI6221\Project\TestImage.JPG')
#print(img.shape)

path = r"C:\Users\79109\gm\workplace\BlindWaterMarking-python\blindwatermarking\catalog\media\bwm_original_image.jpg"
#h = re.findall(r'(?:[A-Z]:|\\|(?:\.{1,2}[\/\\])+)[\w+\\\s_\(\)\/]+(?:\.\w+)*', path)
h = re.findall(r"(.+\\).+?\.", path)
print(h)

