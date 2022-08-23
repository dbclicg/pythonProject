from PIL import Image
import math
import operator
from functools import reduce


def image_Contrast(img1, img2):
    """图片对比相似度"""
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result

