from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import background_creator


def wordcloud_generator(year):
    background_creator.create_bg_image(year)

    text_file = open(year+"_Output.txt", "r")
    text = text_file.read()
    text_list = text.split(' ')
    text_file.close()

    # blacklist = ['India', 'States', 'states', 'State', 'Centre', 'Government', 'government', 'govt', 'govt.', 'Govt.', 'will', 'day', 'seek', 'seeks', 'say', 'says',',', '.', '-', 'Congress', 'Cong', 'BJP', 'today', 'Modi', 'police']
    blacklist = ['will', 'seek', 'seeks', 'say', 'Say', 'says',',', '.', '-','today','may','take','meet', 'get','gets','day', 'set', 'nearby', 'Nearby', 'NEARBY', 'NEARby']

    for item in blacklist:
        if item in text_list:
            text_list = [element for element in text_list if element != item]

    text =  ' '.join(text_list)

    mask = np.array(Image.open("output.png"))

    wc = WordCloud(background_color="white", max_words=2000, mask=mask, contour_width=0.1, contour_color='white')

    wc.generate(text)

    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(year+'.png', bbox_inches = 'tight',pad_inches = 0, dpi=400)

for year in ['2014']:
    wordcloud_generator(year)

# plt.show()