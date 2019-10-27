
import pandas as pd
from wordcloud_cn import generate_cn_word_cloud_and_save

df = pd.read_csv('./reviews/Mainland_China/reviews_Mainland_China_2019_10_27.csv')

title_series = " / ".join(df.title)
generate_cn_word_cloud_and_save(title_series, './results/cn_titles.png')

review_series = " / ".join(df.review)
generate_cn_word_cloud_and_save(review_series, './results/cn_reviews.png')