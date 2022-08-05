#Import python Pillow library
from genericpath import isfile
from PIL import Image

import os
#Import aspose words for python for creating html text

import zipfile

#Specify icon sizes to convert and download as .ico 3 sizes
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256 )]
#There is need to automatically check & accept different file formats such as".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"
#If there is an attempt to upload something else it show error
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}
# A function to check if the file is allowed

def createHtml():

    createHtml = open("attest.html","w")

    createHtml.write('<html>\n<head>\n<link rel="icon" type="image/ico" sizes="16x16" href="/Favicon16.ico">\n<link rel="icon" type="image/ico" sizes="24x24" href="/Favicon24.ico">\n<link rel="icon" type="image/ico" sizes="32x32" href="/Favicon32.ico">\n<link rel="icon" type="image/ico" sizes="48x48" href="/Favicon48.ico">\n<link rel="icon" type="image/ico" sizes="64x64" href="/Favicon64.ico">\n<link rel="icon" type="image/ico" sizes="128x128" href="/Favicon128.ico">\n<link rel="icon" type="image/ico" sizes="256x256" href="/Favicon256.ico">\n<link rel="icon" type="image/ico" sizes="270x270" href="/Favicon270.ico">\n<link rel="manifest" href="/site.webmanifest">\n<meta name="msapplication-TileColor" content="#da532c">\n<meta name="theme-color" content="#ffffff">\n</head>\n<body>\n</body>\n</html>'
) 

    createHtml.close()

file_path = input("Please enter the FILENAME you want to convert(sample1.jpg, sample2.png, sample3.webp, sample4.gif, sample5.bmp, sample6.tiff, sample7.jpeg) or FILEPATH: ")
if os.path.isfile(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension.lower() in ALLOWED_EXTENSIONS:
        print("IT'S AN IMAGE FILE")
        #This is where the actual conversion happens
        image = Image.open(file_path)
        fileoutpath = 'Favicon'
        for size in icon_sizes:
            print(size[0])
            fileoutname = fileoutpath + str(size[0]) + ".ico" 
            new_image = image.resize(size)
            new_image.save(fileoutname)
        createHtml()
    else:
        print("IT'S NOT AN IMAGE FILE")

#Returns the converted icon with a new filename + one more size of 128px
new_logo_ico_filename = fileoutpath + "270.ico"
new_logo_ico = image.resize((270, 270))
new_logo_ico.save(new_logo_ico_filename, format="ICO", quality=90)

#Zip the converted icons/HTML codes in a .zip file
filenames = ["Favicon16.ico", "Favicon24.ico", "Favicon32.ico", "Favicon48.ico", "Favicon64.ico", "Favicon128.ico", "Favicon256.ico", "Favicon270.ico", "attest.html",]
with zipfile.ZipFile("multiple_files.zip", mode="w") as archive:
    for filename in filenames:
        archive.write(filename)


#NOTE:
#Before running the above code loclly, make sure to:
#1 Install .NET Extension pack as VSCode extention
#2 Install Pillow using pip install pillow on your VSCode terminal
#3 Install aspose.words using pip install aspose.words on your VSCode terminal

