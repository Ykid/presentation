import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from countries import eng_country_dic

wordnet_lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')


def split_eng_sentences(series: pd.Series) -> pd.Series:
    lowered = " .".join(series).lower()
    return pd.Series(tokenizer.tokenize(lowered)).map(lambda w: wordnet_lemmatizer.lemmatize(w, pos="v"))


def generate_word_cloud_plot(word_series: pd.Series, stop_words, file_path=None):
    # Create and generate a word cloud image:
    text = " ".join(word_series)
    print("There are {} words in the input series.".format(len(text)))
    wordcloud = WordCloud(stopwords=stop_words, background_color="white", width=1520, height=1020, random_state=42,
                          collocations=False).generate(text)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    if not file_path:
        plt.show()
    else:
        plt.savefig(file_path)


eng_stopwords = set(STOPWORDS)
eng_stopwords.update({'goodnotes', 'goodnote', 'note', 'notes', 'app', 'use'})


def generate_title_and_review_plot(path: str, stop_words, country_code: str):
    title_fig_path = f"./results/{country_code}_titles.png"
    review_fig_path = f"./results/{country_code}_reviews.png"
    reviews = pd.read_csv(path)
    title_series = split_eng_sentences(reviews.title)
    review_series = split_eng_sentences(reviews.review)
    generate_word_cloud_plot(title_series, stop_words, title_fig_path)
    generate_word_cloud_plot(review_series, stop_words, review_fig_path)


us_path = "./reviews/United_States/reviews_United_States_2019_10_27.csv"
generate_title_and_review_plot(us_path, eng_stopwords, eng_country_dic["United_States"])

hk_path = "./reviews/HongKong/reviews_HongKong_2019_10_27.csv"
generate_title_and_review_plot(hk_path, eng_stopwords, eng_country_dic["HongKong"])

india_path = "./reviews/India/reviews_India_2019_10_27.csv"
generate_title_and_review_plot(india_path, eng_stopwords, eng_country_dic["India"])

philip_path = "./reviews/Philippines/reviews_Philippines_2019_10_27.csv"
generate_title_and_review_plot(philip_path, eng_stopwords, eng_country_dic["Philippines"])

aus_path = "./reviews/Australia/reviews_Australia_2019_10_27.csv"
generate_title_and_review_plot(aus_path, eng_stopwords, eng_country_dic["Australia"])

ca_path = "./reviews/Canada/reviews_Canada_2019_10_27.csv"
generate_title_and_review_plot(ca_path, eng_stopwords, eng_country_dic["Canada"])
