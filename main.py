from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import Crawler as cw


fileName = cw.Crawl()
text = open(fileName).read()
openImage = input("Enter the name of the .png image file: ")
openImage = openImage + ".png"
python_mask = np.array(PIL.Image.open(openImage))

colormap = ImageColorGenerator(python_mask)

wc = WordCloud(mask=python_mask,
               background_color="white",
               contour_color="black",
               contour_width = 2,
               min_font_size= 3).generate(text)
wc.recolor(color_func=colormap)
#save the wordcloud as a png file
wc.to_file("wordcloud.png")
plt.imshow(wc)
plt.axis("off")
plt.show()



