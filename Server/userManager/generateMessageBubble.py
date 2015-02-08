__author__ = 'tyan'
from PIL import Image
import PIL
import os
from userManager.models import *
from django.contrib.auth.models import User

size = 25, 25
bubbleSize = 40, 40

def generateMB(pic):
    pic = os.getcwd() + '/../media/' + pic.name
    print pic
    f, e = os.path.splitext(pic)
    bubbleFile = os.getcwd() + '/../media/user/bubble.png'
    outfile = f + "_MB.png"
    #try:
    mPic = Image.open(pic)  #.save(outfile)
    bubble = Image.open(bubbleFile)

    bubble.thumbnail(bubbleSize)

    mPic.thumbnail(size, PIL.Image.BILINEAR)
    h, w = mPic.size
    box = (8, 6, 8+h, 6+w)
    bubble.paste(mPic, box, 0)
    bubble.save(outfile)
    # except IOError:
    #     print("cannot finish!", pic)


def run():
    user = User.objects.get(id=1)
    ui = UserInformation.objects.get(user=user)
    generateMB(ui.portrait)
