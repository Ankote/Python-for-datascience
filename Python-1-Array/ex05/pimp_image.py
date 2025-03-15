import numpy as np
import imageio.v3 as iio  # Use imageio to load images
from matplotlib import pyplot as plt
import array


def ft_invert(array) -> array:
    """Inverting a color means changing it to its opposite\
 color. Think of a photo negative—black becomes white,\
 white becomes black, and colors flip to their opposites.
 so we subtract each value from 255."""
    inverted = 255 - array
    return inverted


def ft_red(array) -> array:
    """Keep only the red channel (RGB format)."""
    red_filter = array.copy()
    red_filter[:, :, 1] = 0  # Set green channel to 0
    red_filter[:, :, 2] = 0  # Set blue channel to 0
    return red_filter


def ft_green(array) -> array:
    """Keep only the green channel (RGB format)."""
    green_filter = array.copy()
    green_filter[:, :, 0] = 0  # Set red channel to 0
    green_filter[:, :, 2] = 0  # Set blue channel to 0
    return green_filter


def ft_blue(array) -> array:
    """Keep only the blue channel (RGB format)."""
    blue_filter = array.copy()

    # using for loop
    # for line in blue_filter:
    #     for col in line:
    #         col[0] = 0
    #         col[1] = 0

    # using slicing
    blue_filter[:, :, 0] = 0  # Set red channel to 0
    blue_filter[:, :, 1] = 0  # Set green channel to 0
    print(blue_filter)
    return blue_filter


def ft_grey(array) -> array:
    """Convert an image to grayscale using the luminance formula."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("Input array must be\
             a 3D array with shape (height, width, 3).")
    # Apply the grayscale conversion formula (RGB format)
    gray_filter = 0.299 * array[:, :, 0]\
        + 0.587 * array[:, :, 1]\
        + 0.114 * array[:, :, 2]
    gray_filter = np.clip(gray_filter, 0, 255).astype(np.uint8)
    print(gray_filter.shape)
    return gray_filter


def main():
    # Load the image using imageio (RGB format)
    img = iio.imread('landscape.jpg')

    # Create a 2x3 grid for the subplots (2 rows and 3 columns)
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # Display images in the first row
    axes[0, 0].imshow(img)
    axes[0, 0].set_title('Figure VIII.1: Original')

    axes[0, 1].imshow(ft_invert(img))
    axes[0, 1].set_title('Figure VIII.2: Invert')

    axes[0, 2].imshow(ft_red(img))
    axes[0, 2].set_title('Figure VIII.3: Red')

    # Display images in the second row
    axes[1, 0].imshow(ft_green(img))
    axes[1, 0].set_title('Figure VIII.4: Green')

    axes[1, 1].imshow(ft_blue(img))
    axes[1, 1].set_title('Figure VIII.5: Blue')

    axes[1, 2].imshow(ft_grey(img), cmap='gray')  # Use grayscale colormap
    axes[1, 2].set_title('Figure VIII.6: Grey')

    plt.tight_layout()  # Automatically adjusts spacing
    plt.show()


if __name__ == "__main__":
    main()
