from PIL import Image
import io
import base64


def pixel_diff(rgb1, rgb2):
    """ Returns RGB values equal to the absolute difference of rgb1 and rgb2 """

    for ele1, ele2 in zip(rgb1, rgb2):
        yield abs(ele1 - ele2)


def image_data(path):
    """ Returns base64 encoded data of an image file """

    im = Image.open(path)
    im = im.convert("RGB")

    data = io.BytesIO()
    im.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data


def image_diff(image1_path, image2_path):
    """ Get the absolute difference in RGB values of two images, per-pixel """

    image_one = Image.open(image1_path).convert("RGB")
    image_two = Image.open(image2_path).convert("RGB")
    width, height = image_one.size

    res = Image.new(mode="RGB", size=image_one.size)
    res_pixel_map = res.load()

    for i in range(width):
        for j in range(height):
            if image_one.getpixel((i, j)) != image_two.getpixel((i, j)):
                res_pixel_map[i, j] = tuple(
                    pixel_diff(image_one.getpixel((i, j)), image_two.getpixel((i, j))))

    # Converts image to base64 so it can be displayed in HTML
    data = io.BytesIO()
    res.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data
