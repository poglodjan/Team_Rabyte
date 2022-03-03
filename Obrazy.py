import numpy
from PIL import Image

##################################################

def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size)==2 
    return (numpy.array(img)/255).reshape(img.size[1], img.size[0]).tolist()

def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img)*255).astype(numpy.int8), 'L')
    img.save(filepath)

##################################################

def negatyw(macierz):
    l_wierszy=len(macierz)
    l_kolumn=len(macierz[0])
    for w in range(l_wierszy):
        for k in range(l_kolumn):
            macierz[w][k]=1-macierz[w][k]
    return macierz

def przeksztalcaj(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]=1-A[i][j]
    return A

def kolory(image):
    red, green, blue = image.split()
    new_image = Image.merge("RGB", (red, blue, green))
    new_image.save('result.jpg')

def usun_kolor(image_data,image):
    height,width = image.size
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = image_data[loop1,loop2]
            image_data[loop1,loop2] = 0,g,b
    image.save('changed.jpeg')

def main():
    m=0
    image = Image.open('cars.png')
    image_data = image.load()
    usun_kolor(image_data,image)

if __name__ == '__main__':
   main()

