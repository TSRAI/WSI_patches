# WSI_patches
Patch extraction methods for Whole Slide Images (WSIs). 

## First Method: Extract all patches

This script uses openslide-python to extract tissue patches from a Whole Slide Image (WSI). A WSI is tiled up and every patch from a predefined magnification level are extracted and saved into the output directory. Each patch will be labelled with a 

Run the script in the command line as:

~~~
python patch_extractor_1.py --slide_dir = "WSI/slide.npdi" --output_dir= "output"
~~~
where you predefine the location of the WSI and the output directory for the saved patches.

Optional arguments also include the magnification level (default at the highest "0") and the desired size of the patch (256 x 256 pixels):
~~~
--level=0
--patchsize=256
~~~
