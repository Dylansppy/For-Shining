# -*- encoding: utf-8 -*-

# WordCloud

from wordcloud import WordCloud
from matplotlib.image import imread
import matplotlib.pyplot as plt

filename = "chat.txt"

with open(filename, encoding='UTF-8') as f:
    mytext = f.read()

# print(mytext)

mask_color_path = "bg.jpg"  # 设置背景图片路径
font_path = '/Library/Fonts/WCL-03.ttf'  # 为matplotlib设置中文字体路径没;路径需要改成你本地的字体路径,若是全英文,也可不设字体路径
imgname1 = "en_WordCloud_DefautColors.png"  # 保存的图片名字1(只按照背景图片形状)
imgname2 = "en_WordCloud_ColorsByImg.png"  # 保存的图片名字2(颜色按照背景图片颜色布局生成)
width = 1000
height = 200
margin = 2

# 设置背景图片
mask_coloring = imread(mask_color_path)
wc = WordCloud(font_path=font_path,
               background_color="white",  # 背景颜色
               max_words=200,  # 词云显示的最大词数
               mask=mask_coloring,  # 设置背景图片
               max_font_size=200,  # 字体最大值
               # random_state=42,
               width=width, height=height, margin=margin,
               )
wc.generate(mytext)

plt.figure()
# 以下代码显示图片
# 绘制词云
plt.imshow(wc)
plt.axis("off")
plt.show()

# 保存图片
wc.to_file(imgname1)
wc.to_file(imgname2)