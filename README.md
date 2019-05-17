# WSI_patches
A patch extraction method for Whole Slide Images (WSIs). This method will create patches without using predefined annotations. Otsu Thresholding and binary dilation is used to determine whether a patch contains sufficient tissue. As a result, this method will allow you save patches with or without tissue. An example tissue patch (256 x 256 pixels) is presented below: 

<img src = "images/86844-113664-34560.png"

## Requirements
Before you get started, a requirments.txt file has been provided so you can install all the relevant dependencies for these extraction methods. Navigate to the directory contaning this file and type the following command in your terminal to install these packages:
~~~
pip install -r requirements.txt
~~~

## Extract patches

We will use openslide-python to extract tissue patches from a Whole Slide Image (WSI). Every patch from a predefined magnification level is extracted and saved into the output directory. Each patch will be labelled with the patch ID and location of the patch. The output directory is automatically created for the saved patches.

To execute the patch extraction you must predefine the location of the directory containing the WSIs. You also have the option to either save patches that contain tissue only (True) or save every patch from the whole slide image (False). 

Type in the following commands in the command line:
~~~
python patch_extractor.py --slide_dir = WSI --tissue_only True
~~~

Optional arguments also include specifying the magnification level (default at the highest, "0") and specifying the desired size of the patch (256 x 256 pixels):
~~~
python patch_extractor.py --slide_dir = WSI --tissue_only True --level 0 --patchsize 256
~~~
