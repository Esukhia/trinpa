from collections import defaultdict
from pathlib import Path

import numpy as np

from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude


def getFrequencyDictForText(text):
    text = text.replace('\n', ' ')
    fullTermsDict = defaultdict(int)

    for word in text.split(" "):
        fullTermsDict[word] += 1

    return fullTermsDict


def makeImage(text, mask_file, out_file, font_path, max_font_size, rel_scal, bckgrnd_file):
    cloud_color = np.array(Image.open(mask_file))

    mask = cloud_color.copy()
    mask[mask.sum(axis=2) == 0] = 255

    # generate word cloud
    wc = WordCloud(font_path=str(font_path), mask=mask, background_color=None, repeat=True,
                   mode='RGBA', max_font_size=max_font_size, relative_scaling=rel_scal)
    wc.generate_from_frequencies(text)

    # create coloring from image
    image_colors = ImageColorGenerator(cloud_color)
    image_colors.default_color = [0.6, 0.6, 0.6]
    wc.recolor(color_func=image_colors)

    # write to file
    plt.imshow(wc, interpolation="bilinear")

    wc.to_file(out_file)

    if bckgrnd_file:
        img = Image.open(out_file)
        bckgrnd = Image.open(bckgrnd_file)
        bckgrnd.paste(img, (0, 0), img)
        bckgrnd.save(out_file, 'PNG')


def gen_word_cloud(in_text, out_file, mask_file, background_file=None, font_path=None, max_font_size=150, relative_scaling=0.5):
    # prepare text
    text = Path(in_text).read_text()
    text = getFrequencyDictForText(text)
    # gen wordcloud
    font_path = Path(__file__).parent / 'monlam_uni_ouchan2.ttf' if not font_path else Path(font_path)

    mask = Path(mask_file)
    makeImage(text, mask, out_file, font_path, max_font_size, relative_scaling, background_file)
