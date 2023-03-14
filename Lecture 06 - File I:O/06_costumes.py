# Create our own animated GIF
#
# PIL is the Python Imaging Library: https://pypi.org/project/Pillow/
# It permits to manipulate images in Python.
#     pip install Pillow

import sys
from PIL import Image

def costume():
    images = []
    for arg in sys.argv[1:]:  # skip the first argument, which is the script name
        image = Image.open(arg)  # to make the image manipulable
        images.append(image)
    
    images[0].save(
        "costumes.gif",
        save_all=True,  # save all the frames
        append_images=images[1:],  # append the next images, in this case just 1
                                   # hence it would have been enough write [images[1]]
                                   # remembering the square brackets to make it a list
        duration=200,  # duration of each frame in ms
        loop=0  # loop forever
    )



def main():
    if len(sys.argv) != 3 or sys.argv[1] != 'costume1.gif' or sys.argv[2] != 'costume2.gif':
        sys.exit(f"Usage: python {sys.argv[0]} costume1.gif costume2.gif")

    costume()


if __name__ == '__main__':
    main()


# This was just the beginning of file manipulation in Python. There are many other
# possibilities, e.g., to manipulate audio files, documents, binary files, etc.