import imageio.v3 as iio
import array


def ft_load(path: str) -> array:
    """Function loads an image, prints its format, and its pixels\
content in RGB format."""
    SUPORTED_TYPE = ['.png', '.jpg', '.jpeg']
    if path[-4:] not in SUPORTED_TYPE and path[-5:] not in SUPORTED_TYPE:
        print("Error : unsupported type")
        return
    try:
        img = iio.imread(path)
        lines, cols, rgb = img.shape
        print(f"The shape of image is: ({lines}, {cols}, {rgb})")
        print(img)
        return img
    except Exception as e:
        print(e)


def main():
    print(ft_load.__doc__)


if __name__ == "__main__":
    main()
