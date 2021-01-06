import sys
import random
import argparse
from PIL import Image


parser = argparse.ArgumentParser(description='Image processing script.')


def flip_lr(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def flip_ud(image):
    return image.transpose(Image.FLIP_UP_DOWN)


def rotate(image, theta, fill=None):
    if fill:
        background = Image.new(mode=image.mode,size=image.size,color=fill)
        return Image.alpha_composite(background, image.rotate(theta))
    else:
        return image.rotate(theta)


def translate_lr(image, amt):
    pass

def translate_ud(image,amt):
    pass


def random_rotate(image, lower_bound, upper_bound, fill=None):
    return rotate(image, random.randint(lower_bound, upper_bound), fill)


def main():
    args = parser.parse_args()


    # try:
    #     image = Image.open(sys.argv[1])
    # except IndexError:
    #     print ('[-]Input valid image file')
    # except FileNotFoundError:
    #     print ('[-]Input valid file path')

    # proc_image = rotate(flip_lr(image),69,'#FFFF00')
    # proc_image.show()



if __name__ == '__main__':
    main()
