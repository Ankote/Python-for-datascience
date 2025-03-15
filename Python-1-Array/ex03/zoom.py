from matplotlib import pyplot as plt
from load_image import ft_load
from skimage.transform import resize


def ft_zoom(img, zoom_factor=1.5):
    """Zooms into the center of the image by a given zoom factor."""
    h, w, chanels = img.shape
    new_h, new_w = int(h / zoom_factor), int(w / zoom_factor)
    start_h, start_w = (h - new_h) // 2, (w - new_w) // 2
    cropped_img = img[start_h:h - start_h, start_w:w - start_w]
    zoomed_img = resize(cropped_img, (h, w), anti_aliasing=True)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(zoomed_img)
    axes[1].imshow(img)
    axes[0].set_title('zoomed img')
    axes[1].set_title('Original image')
    print(f"New shape after slicing: {zoomed_img.shape}")
    plt.show()
# Load the image


def main():
    img = ft_load("animal.jpeg")  # Load image as NumPy array
    ft_zoom(img, zoom_factor=3)


if __name__ == "__main__":
    main()
