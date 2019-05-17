# WSI_patches
A patch extraction method for Whole Slide Images (WSIs). This method will create patches with no predefined annotations and can be used for methods using "weakly-labelled" images. 

## Requirements
Before you get started, a requirments.txt file has been provided so you can install all the relevant dependencies for these extraction methods. Simply type the following command in your terminal to install these packages:
~~~
pip install -r requirements.txt
~~~

## Extract patches

We will use openslide-python to extract tissue patches from a Whole Slide Image (WSI). A WSI is tiled up and every patch from a predefined magnification level are extracted and saved into the output directory. Each patch will be labelled with the patch ID and location of the patch. 

To execute the patch extraction you must predefine the location of the directory containing the WSIs. The output directory is automatically created for the saved patches.

Run the script in the command line as:

~~~
python patch_extractor.py --slide_dir = "WSI/slide.npdi" 
~~~

Optional arguments also include the magnification level (default at the highest "0") and the desired size of the patch (256 x 256 pixels):
~~~
python patch_extractor.py --slide_dir = "WSI/slide.npdi" --level=0 --patchsize=256
~~~
