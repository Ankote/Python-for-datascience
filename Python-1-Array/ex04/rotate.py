import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt


def ft_rotate(img):
    """
Image Rotation Script
This script loads an image, transposes it\
 (swapping its width and height), and displays both
 the original and transposed images using Matplotlib.

Functions:
-----------
- ft_rotate(img):
    Takes an image as a NumPy array,\
 transposes it, and displays both the original and
    transposed images.

- main():
    Loads an image using `ft_load` and calls `ft_rotate` on it.

Usage:
-------
Run the script directly to see the original and transposed images.

Dependencies:
--------------
- numpy
- matplotlib
- load_image.ft_load (for loading the image)
"""

    h, w, channels = img.shape

    rotated_imge = np.zeros((w, h, channels), dtype=img.dtype)
    for i in range(w):
        for j in range(h):
            rotated_imge[i, j] = img[j, i]
    print(f"New shape after Transpose: {rotated_imge.shape}", )
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img)
    axes[1].imshow(rotated_imge)
    axes[0].set_title('normal image')
    axes[1].set_title('transposed image')
    plt.show()


def main():
    ft_rotate(ft_load("animal.jpeg"))


if __name__ == "__main__":
    main()
