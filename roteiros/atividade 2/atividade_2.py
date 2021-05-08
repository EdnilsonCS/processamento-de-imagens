import numpy as np
import matplotlib.pyplot as plt 
from skimage import data
from PIL import Image
import math

image = data.coffee()
plt.imshow(image, cmap='gray')


def convert_to_gray(image, luma=False):
    if luma:
        params = [0.299, 0.589, 0.114]
    else:
        params = [0.2125, 0.7154, 0.0721]    
    gray_image = np.ceil(np.dot(image[...,:3], params))
 
    # Saturando os valores em 255
    gray_image[gray_image > 255] = 255
    
    return gray_image


def instantiate_histogram():    
    hist_array= []
    
    for i in range(0,256):
        hist_array.append(str(i))
        hist_array.append(0)
    
    hist_dct = {hist_array[i]: hist_array[i + 1] for i in range(0, len(hist_array), 2)} 
    
    return hist_dct
    histogram = instantiate_histogram()



def count_intensity_values(hist, img):
    for row in img:
        for column in row:
            hist[str(int(column))] = hist[str(int(column))] + 1
     
    return hist
    histogram = count_intensity_values(histogram, image)


def plot_hist(hist, hist2=''):
    if hist2 != '':
        figure, axarr = plt.subplots(1,2, figsize=(20, 10))
        axarr[0].bar(hist.keys(), hist.values())
        axarr[1].bar(hist2.keys(), hist2.values())
    else:
        plt.bar(hist.keys(), hist.values())
        plt.xlabel("Níveis intensidade")
        ax = plt.gca()
        ax.axes.xaxis.set_ticks([])
        plt.grid(True)
        plt.show()


def get_hist_proba(hist, n_pixels):
    hist_proba = {}
    for i in range(0, 256):
        hist_proba[str(i)] = hist[str(i)] / n_pixels
    
    return hist_proba
    n_pixels = image.shape[0] * image.shape[1]
    hist_proba = get_hist_proba(histogram, n_pixels) 



def get_accumulated_proba(hist_proba): 
    acc_proba = {}
    sum_proba = 0
    
    for i in range(0, 256):
        if i == 0:
            pass
        else: 
            sum_proba += hist_proba[str(i - 1)]
            
        acc_proba[str(i)] = hist_proba[str(i)] + sum_proba
    
    return acc_proba
    accumulated_proba = get_accumulated_proba(hist_proba)





def get_new_gray_value(acc_proba):
    new_gray_value = {}
    
    for i in range(0, 256):
        new_gray_value[str(i)] = np.ceil(acc_proba[str(i)] * 255)
    return new_gray_value
    new_gray_value = get_new_gray_value(accumulated_proba)



def equalize_hist(img, new_gray_value):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            img[row][column] = new_gray_value[str(int(img[row] [column]))]
            
    return img 




eq_img = equalize_hist(image.copy(), new_gray_value)
figure, axarr = plt.subplots(1,2, figsize=(20, 10))
axarr[0].imshow(image, cmap='gray')
axarr[1].imshow(eq_img, cmap='gray')       