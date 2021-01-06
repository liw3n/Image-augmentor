import os
import random
import argparse
from PIL import Image, UnidentifiedImageError


parser = argparse.ArgumentParser(description='Image processing script.')
parser.add_argument('-i', '--input', help='Input file/directory path to peform image augmentation on', required=True)
parser.add_argument("--flr", help='Perform a left right flip on the image', action="store_true")
parser.add_argument("--ftb", help='Perform a top bottom flip on the image', action="store_true")
parser.add_argument("--tlr", metavar='AMOUNT', help='Perform a left right translation on the image by a certain AMOUNT', type=int)
parser.add_argument("--tud", metavar='AMOUNT', help='Perform an up down translation on the image by a certain AMOUNT', type=int)
parser.add_argument("--rot", metavar="DEGREES", help='Perform an image rotation by the specified DEGREES counter clockwise (-ve for clockwise rotation)', type=int )
parser.add_argument("--ranrot", help='Perform a counterclockwise image rotation by a certain number of degrees randomly chosen between LOWERBOUND and UPPERBOUND (-ve for clockwise rotation)',
                    metavar=("LOWERBOUND","UPPERBOUND"), nargs=2, type=int )
parser.add_argument("--fill", metavar='HEX', help='Replace any newly introduced alpha pixels with pixels of a certain HEX value during any geometric image transformation', type=str)


def flip_left_right(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def flip_top_bottom(image):
    return image.transpose(Image.FLIP_TOP_BOTTOM)


def rotate(image, theta, fill):
    return image.rotate(theta, fillcolor=fill)


def translate_left_right(image, amt, fill):
    pass


def translate_up_down(image,amt, fill):
    pass


def logic_handler(image,args):
    fill = args.fill
    if args.flr:
        flip_left_right(image).show()
    if args.ftb:
        flip_top_bottom(image).show()
    if args.rot:
        rotate(image, args.rot, fill).show()
    if args.ranrot:
        if args.ranrot[0] < args.ranrot[1]:
            rotate(image, random.randint(args.ranrot[0], args.ranrot[1]), fill).show()
        else:
            print('[-]LOWERBOUND must be smaller than UPPERBOUND')
    if args.tlr:
        translate_left_right(image, args.tlr, fill)
    if args.tud:
        translate_up_down(image, args.tud, fill)


def main():
    args = parser.parse_args()

    if os.path.isfile(args.input):
        try:
            image = Image.open(args.input)
            logic_handler(image, args)
        except UnidentifiedImageError:
            print ("[-]Invalid image file provided")
    elif os.path.isdir(args.input): #INCOMPLETE
        os.chdir(args.input)
        for i in os.listdir(os.getcwd()):
            try:
                image = Image.open(i)
                logic_handler(image, args)
            except UnidentifiedImageError:
                print (f"[-]Invalid image file '{i}' in provided directory")
                return
    else:
        print (f"[-]'{args.input}' is neither a valid filepath or directory path")


if __name__ == '__main__':
    main()
