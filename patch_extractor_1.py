# import all libraries
import os, sys
import openslide
import argparse
import PIL.ImageOps

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--slide_dir', type=str, default='WSI/',
                       help='data directory containing whole slide image')
    parser.add_argument('--level', type=int, default= 0,
                       help='the magnification of the whole slide image, highest magnification at level 0')
    parser.add_argument('--patchsize', type=int, default= 256,
                       help='the size of the extracted patch, the default is 256 x 256 pixels')
    parser.add_argument('--output_dir', type=str, default='output/',
                       help='the output directory for the extracted patches')

    args = parser.parse_args()
    patch_extractor(args)



def open_slide(slide):
    """
    A function to read and open a WSI using openslide.

    Args:
    The path to the WSI.

    Returns:
    An openslide WSI object
    """
    try:
        wsi = openslide.OpenSlide(slide)
        print("An openslide object has been created.")
    except RuntimeError:
        raise RuntimeError('I was unable to read your WSI file: {}'.format(slide))
    return wsi




def patch_extractor(args):
    """
    A function that extracts patches from a whole slide image.

    Args:
    The path to the whole slide image and output directory. Optionally you can
    also define the magnification level of the slide and patch size that you
    want to extract.

    Returns:

    A patch image labelled with the id number and location.

    """
    wsi = open_slide(args.slide_dir)
    width, height = wsi.dimensions #dimensions A (width, height) tuple for level 0 of the slide.
    print("The dimensions of the whole slide image is width: ", width, " and height: ", height)
    idx = 0
    for i in range(int(height/args.patchsize)):
        print ("iteration %d out of %d"%(i+1, int(height/args.patchsize)))
        for j in range(int(width/args.patchsize)):
            patch = wsi.read_region(location=(j*args.patchsize,i*args.patchsize), level=args.level,
                                    size=(args.patchsize, args.patchsize)).convert('RGB')
            patch.save(args.output_dir + "%s-%s-%s.png"% (idx, j*args.patchsize, i*args.patchsize))
            idx += 1


if __name__ == '__main__':
    main()
