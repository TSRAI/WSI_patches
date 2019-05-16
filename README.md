# WSI_patches
Patch extraction methods for Whole Slide Images (WSIs). 

## First Method: All patches

This script uses openslide-python to extract tissue patches from a Whole Slide Image (WSI). A WSI is tiled up and every patch from a predefined magnification level are extracted and saved into the output directory.

Run the script in the command line as:

~~~
python patch_extractor_1.py --slide_dir = "WSI/slide.npdi" --output_dir= "output"
~~~

Optional arguments include
~~~
--level=0 
--patchsize=256
~~~
