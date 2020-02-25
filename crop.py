import numpy
import os
import cv2

dir_name = r'C:\Users\Maria\Desktop\Geovision\New GV003 Images\WET'
output_dir = r'C:\Users\Maria\Desktop\Geovision\New GV003 Images\WET'
list_of_files = os.listdir(dir_name)

x1 = 288 # left
x2 = 8381 # right
y = [1680, 2380, 3090,3700] # top y interval
ycheat = [2416, 3105,3760, 4450] # bottom y interval

for foldername in list_of_files:
    folderpath = dir_name + '/' + foldername
    filename = os.listdir(folderpath)
    filename = ''.join(filename[1])
    filepath = folderpath+'/'+ filename
    # read image in
    img = cv2.imread(filepath)
    
    for i in range(0,len(y)):
        crop_img = img[y[i]:ycheat[i], x1:x2]
        cv2.imwrite(output_dir+'/'+ foldername + '_'+ str(i+1)+ '.jpg',crop_img)

