import jieba
from os import path
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud

# Setting up parallel processes :4 ,but unable to run on Windows
jieba.enable_parallel(4)

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
d = d + '/cn'

stopwords_path = d + '/wc_cn/stopwords_cn_en.txt'
# Chinese fonts must be set
font_path = d + '/fonts/SourceHanSerif/SourceHanSerifK-Light.otf'

# if you want use wordCloud,you need it
# add userdict by add_word()
userdict_list = []


# The function for processing text with Jieba
def jieba_processing_txt(text):
    for word in userdict_list:
        jieba.add_word(word)

    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)

    with open(stopwords_path, encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.splitlines()

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)


def generate_cn_word_cloud(text):
    wc = generate_word_cloud(text)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    return plt


def generate_cn_word_cloud_and_save(text: str, file_path: str):
    wc = generate_word_cloud(text)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(file_path)


def generate_word_cloud(text: str):
    wc = WordCloud(font_path=font_path, background_color="white", max_words=200, width=1000, height=860,
                   random_state=42)
    wc.generate(jieba_processing_txt(text))
    return wc
