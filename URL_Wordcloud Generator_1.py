import json
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime


url_base = "https://www.thehindu.com/archive/print"

year_list = list(range(2014,2015))
month_list = list(range(1,13))
date_list = list(range(1,32))

data_list = []

for year in year_list:
    for month in month_list:
        for date in date_list:
            url = url_base+"/"+str(year)+"/"+str(month)+"/"+str(date)+"/"
            try:
                if(datetime(year,month,date)):
                    response = requests.get(url)
                    if response.ok:
                        try:
                            print(url)
                            data = response.text
                            soup = BeautifulSoup(data, 'html.parser')
                            li_list = soup.find('ul', {'class': 'archive-list'})
                            split_details = list(li_list.stripped_strings)
                            data_list.append(split_details)
                        except AttributeError:
                            pass
            except ValueError:
                pass


print(data_list)

text = ''

for element in data_list:
    element_text = ' '.join(element)
    text = text + element_text

print(text)

text_file = open("2014_Output.txt", "w")
text_file.write(text)
text_file.close()

wordcloud = WordCloud().generate(text)

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('2014.png')
plt.show()