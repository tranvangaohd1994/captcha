import cv2
from matplotlib import pyplot as plt
import glob
import numpy as np
from PIL import ImageFont, ImageDraw, Image  

def removeHair():
    allImage = glob.glob('inputD/*png')
    
    for imgLink in allImage:
        print(imgLink.split('\\')[-1][:-4])
        imgL = input("linkImage: ")
        img = cv2.imread(imgL)
        #print(img.shape)
        cv2.imshow('img', img)

        fr_thresh = cv2.inRange(img, (55, 55, 55), (59, 59, 59))

        #ret,thresh1 = cv2.threshold(imagem, 255-50, 255, cv2.THRESH_BINARY)
        fr_thresh = cv2.bitwise_not(fr_thresh)
        cv2.imshow('fr_thresh', fr_thresh)
        cv2.imwrite('inrange.png', fr_thresh)

        cv2.waitKey()
        
def getBackground():
    allImage = glob.glob('inputD/*png')
    for imgLink in allImage:
        print(imgLink.split('\\')[-1][:-4])
        img = cv2.imread(imgLink)
        #print(img.shape)
        cv2.imshow('img', img)

        fr_thresh_1 = cv2.inRange(img, (0, 0, 0), (55, 55, 55))
        
        fr_thresh_1 = cv2.bitwise_not(fr_thresh_1)
        

        #cv2.putText(img,'content',   bottomLeft, font,               fontScale,fontColor,thickness,lineType)
        #---------------putText to image
         # Pass the image to PIL  
        pil_im = Image.fromarray(fr_thresh_1) 
        draw = ImageDraw.Draw(pil_im) 
        font = ImageFont.truetype("font\AGENO___.TTF", 50)   
        draw.text((10, 10), '32de', font=font)  
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR) 
        #cv2.putText(fr_thresh_1, '213g', (50,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 4, 2)
        
        cv2.imshow('cv2_im_processed', cv2_im_processed)
        cv2.waitKey()
        exit()

if __name__ == "__main__":
    print("getbackground function:")
    #getBackground()
    removeHair()
