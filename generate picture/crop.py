import sys, os, re
from PIL import Image

def crop(image_path, coords):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(image_path.replace(".jpg", "_crop.jpg"))

dir_path = os.path.dirname(os.path.realpath(__file__))
allList_back = os.listdir(dir_path)
all_pictures = []
# Setting the regular expression to only look for .jpg extenstion
jpgRE = re.compile('^\w+.jpg$', re.I)
# Removing any files that do not have an .fbx extenstion
for fname in allList_back:
    if jpgRE.search(fname):
        crop(fname, (80, 97, 1180, 1432))
