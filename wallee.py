import os
import ctypes
from PIL import Image
from random import randint
import webcolors
from scipy.spatial import KDTree
from webcolors import hex_to_rgb
import json

#get config-datas
try:
    with open('config.json') as f:
        data = json.load(f)

    path = data["path"]
    maximage = data["maximage"]
    autostart = data["autostart"]

except:
    print("Error reading json File")


#get screensize
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

#delete oldest img when more then 10 images
list_of_files = os.listdir(path)
full_path = ['{}{}'.format(path, x) for x in list_of_files]


while len(list_of_files) >= maximage:
    print(len(list_of_files))
    oldest_file = min(full_path, key=os.path.getctime)
    print(oldest_file)
    os.remove(os.path.abspath(oldest_file))
    list_of_files = os.listdir(path)
    full_path = ['{}{}'.format(path, x) for x in list_of_files]


#generate random 1-color-image
r=randint(0, 255)
g=randint(0, 255)
b=randint(0, 255)

img = Image.new('RGB', (screensize[0], screensize[1]), (r, g, b))


#get color-name (for image name)
def convert_rgb_to_names(rgb_tuple):
    
    # -- a dictionary of all the hex and their respective names in css3
    css3_db = webcolors.CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]

print(convert_rgb_to_names((r,g,b)))

#save image
imgpath = path + f"randomimg{convert_rgb_to_names((r,g,b))}.png"
img.save(imgpath)

#set image as background
ctypes.windll.user32.SystemParametersInfoW(20, 0, imgpath , 0)


