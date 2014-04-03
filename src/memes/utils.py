from PIL import ImageFont
from PIL import Image as PIL_Image
from PIL import ImageDraw


FONT_PATH = '/usr/share/fonts/truetype/msttcorefonts/Impact.ttf'


def draw_text(image, top_text, bottom_text):
    """Draw meme style text on image.

    Strongly inspired by https://github.com/danieldiekmeier/memegenerator

    """
    img = PIL_Image.open(image.name)
    imageSize = img.size
    draw = ImageDraw.Draw(img)

    # Top font
    topFontSize = imageSize[1] / 5
    topFont = ImageFont.truetype(FONT_PATH, topFontSize)
    topTextSize = topFont.getsize(top_text)
    while topTextSize[0] > imageSize[0] - 20:
        topFontSize = topFontSize - 1
        topFont = ImageFont.truetype(FONT_PATH, topFontSize)
        topTextSize = topFont.getsize(top_text)

    # find top centered position for top text
    topTextPositionX = (imageSize[0] / 2) - (topTextSize[0] / 2)
    topTextPositionY = 0
    topTextPosition = (topTextPositionX, topTextPositionY)

    # draw outlines
    outlineRange = topFontSize / 15
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text((topTextPosition[0] + x, topTextPosition[1] + y), top_text, (0, 0, 0), font=topFont)

    draw.text(topTextPosition, top_text, (255, 255, 255), font=topFont)

    # Bottom font
    bottomFontSize = imageSize[1] / 5
    bottomFont = ImageFont.truetype(FONT_PATH, bottomFontSize)
    bottomTextSize = bottomFont.getsize(bottom_text)
    bottomTextSize = (bottomTextSize[0], bottomTextSize[1] + 15)
    while bottomTextSize[0] > imageSize[0] - 20:
        bottomFontSize = bottomFontSize - 1
        bottomFont = ImageFont.truetype(FONT_PATH, bottomFontSize)
        bottomTextSize = bottomFont.getsize(bottom_text)
        bottomTextSize = (bottomTextSize[0], bottomTextSize[1] + 15)

    # find bottom centered position for bottom text
    bottomTextPositionX = (imageSize[0] / 2) - (bottomTextSize[0] / 2)
    bottomTextPositionY = imageSize[1] - bottomTextSize[1]
    bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

    # draw outlines
    outlineRange = bottomFontSize / 15
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text((bottomTextPosition[0] + x, bottomTextPosition[1] + y), bottom_text, (0, 0, 0), font=bottomFont)

    draw.text(bottomTextPosition, bottom_text, (255, 255, 255), font=bottomFont)

    return img


def draw_text_2(image, top_text, bottom_text):
    img = PIL_Image.open(image.name)
    imageSize = img.size

    FONT_PATH = '/usr/share/fonts/truetype/msttcorefonts/Impact.ttf'
    fontSize = imageSize[1] / 5
    font = ImageFont.truetype(FONT_PATH, fontSize)
    topTextSize = font.getsize(top_text)
    bottomTextSize = font.getsize(bottom_text)
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize = fontSize - 1
        font = ImageFont.truetype(FONT_PATH, fontSize)
        topTextSize = font.getsize(top_text)
        bottomTextSize = font.getsize(bottom_text)

    # find top centered position for top text
    topTextPositionX = (imageSize[0] / 2) - (topTextSize[0] / 2)
    topTextPositionY = 0
    topTextPosition = (topTextPositionX, topTextPositionY)

    # find bottom centered position for bottom text
    bottomTextPositionX = (imageSize[0] / 2) - (bottomTextSize[0] / 2)
    bottomTextPositionY = imageSize[1] - bottomTextSize[1]
    bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

    draw = ImageDraw.Draw(img)

    # draw outlines
    # there may be a better way
    outlineRange = fontSize / 15
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text((topTextPosition[0] + x, topTextPosition[1] + y), top_text, (0, 0, 0), font=font)
            draw.text((bottomTextPosition[0] + x, bottomTextPosition[1] + y), bottom_text, (0, 0, 0), font=font)

    draw.text(topTextPosition, top_text, (255, 255, 255), font=font)
    draw.text(bottomTextPosition, bottom_text, (255, 255, 255), font=font)

    return img
