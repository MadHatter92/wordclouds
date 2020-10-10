from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def create_bg_image(text):
    mode = 'RGB' # for color image “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.
    size = (960, 480)
    color = (0, 0, 0)

    im = Image.new(mode, size, color)

    im.save('test.png')

    # img = Image.open("test.png")
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype('/usr/share/fonts/TTF/Hack-Regular.ttf', 60)
    # draw.text((0, 0),"2020",(255,255,255), font=font)
    # img.save('output.png')


    image = Image.open("test.png").convert("RGBA")
    txt = Image.new('RGBA', image.size, (255,255,255,0))
    font = ImageFont.truetype("/usr/share/fonts/cantarell/Cantarell-ExtraBold.otf", 410)
    d = ImageDraw.Draw(txt)   

    d.text((0, 0), text, fill=(255, 255, 255, 255), font=font)

    combined = Image.alpha_composite(image, txt)    

    combined.save("output.png")