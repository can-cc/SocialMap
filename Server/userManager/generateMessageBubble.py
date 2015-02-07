__author__ = 'tyan'
from PIL import Image
import os, sys
from .models import UserInformation
from django.contrib.auth.models import User

size = (25, 25)
bubbleSize = (40, 40)

def generateMB(pic):
    pic = os.getcwd() + '/../media/' + pic.name
    f, e = os.path.splitext(pic)
    bubbleFile = os.getcwd() + '/../media/user/bubble.png'
    outfile = f + "_MB.png"
    outfile2 = f + "_MB2.png"
    #try:
    mPic = Image.open(pic)  #.save(outfile)
    bubble = Image.open(bubbleFile)

    bubble.thumbnail(bubbleSize)
    bubble.save(outfile2)

    mPic.thumbnail(size)
    box = (8, 6, 33, 31)
    bubble.paste(mPic, box, 0)
    bubble.save(outfile)
    # except IOError:
    #     print("cannot finish!", pic)


def run():
    user = User.objects.get(id=1)
    ui = UserInformation.objects.get(user=user)
    generateMB(ui.portrait)
