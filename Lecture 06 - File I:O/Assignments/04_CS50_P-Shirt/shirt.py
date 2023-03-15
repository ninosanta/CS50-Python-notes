# https://pillow.readthedocs.io/en/stable/handbook/
# https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
# https://pillow.readthedocs.io/en/stable/reference/Image.html

import sys
from os.path import isfile
from PIL import Image, ImageOps


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python {sys.argv[0]} <image1> <image2>")
    elif not isfile(sys.argv[1]):
        sys.exit(f"Error: {sys.argv[1]} does not exist")
    elif not sys.argv[1].lower().endswith((".png", ".jpg", "jpg")) or not sys.argv[
        2
    ].lower().endswith((".png", ".jpg", "jpg")):
        sys.exit("Error: invalid extension. File must be: .png, .jpg, or .jpeg")
    elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
        # Another possibility is os.path.splitext(path) that returns a tuple (path, extension)
        sys.exit(
            "Error: both files must have the same extension (.png, .jpg, or .jpeg)"
        )

    overlap_shirt(sys.argv[1], sys.argv[2])


def overlap_shirt(src, dst):
    with Image.open("./shirt.png") as shirt:
        shirt_size = shirt.size  # tuple containing (width, height)
        with Image.open(src) as photo:
            # the shirt is "smaller" than the photo. Hence, we resize the photo
            # to make the shirt fit on it
            shirt_on_photo = ImageOps.fit(photo, shirt_size)
        shirt_on_photo.paste(shirt, shirt)  # paste the shirt on the resized photo
        shirt_on_photo.save(dst)


if __name__ == "__main__":
    main()
