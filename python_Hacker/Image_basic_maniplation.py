from PIL import Image, ImageFilter
im = Image.open( 'Desktop/apple.jpg' )#read the image
im.show()#image display
im_sharp = im.filter( ImageFilter.SHARPEN )#filterng the imaga
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )#saving the image
r,g,b = im_sharp.split()#splitting the image into r,g,b cotext
exif_data = im._getexif()#gettng resultent one