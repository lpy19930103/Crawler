#ocr

from PIL import Image
import subprocess
from urllib.request import urlretrieve


def cleanFile(filePath, newFilePath):
    imgurl = 'http://pythonscraping.com/image_captcha?sid=44408&ts=1516608665'
    urlretrieve(imgurl, 'filepath.jpg')
    image = Image.open(filePath)

    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    subprocess.call(['tesseract', newFilePath, 'output'])

    with open('output.txt', 'r') as outputFile:
        print(outputFile.read())


cleanFile('filepath.jpg', "newfilepath.png")
