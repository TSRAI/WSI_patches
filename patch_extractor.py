"""
Author: Taran Rai

Deepathology Ltd., London, United Kingdom
Centre for Vision, Speech and Signal Processing, University of Surrey, Guildford, United Kingdom

"""

import os, sys
import openslide
import numpy as np
from scipy.ndimage.morphology import binary_dilation
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--slide_dir', type=str, default='WSI/',
                       help='You must specify the data directory containing the whole slide images')
    parser.add_argument('--level', type=int, default= 0,
                       help='The magnification of the whole slide image, the highest magnification is level 0')
    parser.add_argument('--patchsize', type=int, default= 256,
                       help='The size of the extracted patch, the default is 256 x 256 pixels')
    parser.add_argument('--tissue_only', type=str, default= 'True',
                       help='True or False depending on whether you want to extract patches with tissue only')

    args = parser.parse_args()
    if args.tissue_only == 'True':
        args.tissue_only = True
    elif args.tissue_only == 'False':
        args.tissue_only = False
    else:
        raise Exception('Incorrect value for args.tissue_only.  Value of {} given'.format(args.tissue_only))

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
    for root, dirnames, filenames in os.walk(args.slide_dir):
        for file in filenames:
            slide = os.path.join(root,file)
            slide_name = os.path.basename(slide)
            slide_name = slide_name.rstrip(".ndpi")
            wsi = open_slide(slide)
            width, height = wsi.level_dimensions[args.level] #dimensions A (width, height) tuple for level [k] of the slide.
            print("The dimensions of the whole slide image is width: ", width, " and height: ", height)

            outputdir = ("output/%s" % (file))
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)

            idx = 0
            for i in range(int(height/args.patchsize)):
                print ("Loop %d out of %d"%(i+1, int(height/args.patchsize)))
                for j in range(int(width/args.patchsize)):
                    patch = wsi.read_region(location=(j*args.patchsize,i*args.patchsize), level=args.level,
                                            size=(args.patchsize, args.patchsize)).convert('RGB')
                    if args.tissue_only == True:
                        numpy_array = np.array(patch)[:,:,:3]
                        gray = cv2.cvtColor(numpy_array, cv2.COLOR_BGR2GRAY)
                        ret, thresh = cv2.threshold(gray,0,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                        thresh = binary_dilation(thresh, iterations=15)
                        ratio = np.mean(thresh)
                        if ret < 200 and ratio > 0.8:
                            patch.save(outputdir + "/%s-%s-%s-%s.png"% (slide_name, idx, j*args.patchsize, i*args.patchsize))
                    else:
                        patch.save(outputdir + "/%s-%s-%s-%s.png"% (slide_name, idx, j*args.patchsize, i*args.patchsize))

                    idx += 1
            print("PATCH EXTRACTION COMPLETE FOR SLIDE %s" % (file))

if __name__ == '__main__':
    main()
