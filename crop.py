import numpy
import os
import cv2

dir_name = r'C:\Users\Maria\Desktop\Geovision\New GV003 Images\DRY'
output_dir = r'C:\Users\Maria\Desktop\Geovision\New GV003 Images\DRY'
list_of_files = os.listdir(dir_name)

x1 = 250 # left
x2 = 8357 # right

# WET
#y = [1313, 2000, 2689, 3377] 
#ycheat = [2033, 2733, 3398, 4122]

# DRY
y = [1293, 1961, 2633, 3278] # top y interval
ycheat = [1994, 2654, 3310, 4015] # bottom y interval

for foldername in list_of_files:
    folderpath = dir_name + '/' + foldername
    filename = os.listdir(folderpath)
    filename = ''.join(filename[1])
    filepath = folderpath+'/'+ filename
    # read image in
    img = cv2.imread(filepath)
    '''
    # get image height, width
    (h, w) = img.shape[:2]

    # calculate the center of the image
    center = (w / 2, h / 2)

    angle180 = 180
    scale = 1.0

    # 180 degrees
    M = cv2.getRotationMatrix2D(center, angle180, scale)
    img = cv2.warpAffine(img, M, (w, h))
    '''
    
    for i in range(0,len(y)):
        crop_img = img[y[i]:ycheat[i], x1:x2]
        cv2.imwrite(output_dir+'/'+ 'DRY_' + foldername + '_'+ str(i+1)+ '.jpg',crop_img)

