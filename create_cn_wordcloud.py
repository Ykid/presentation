
import pandas as pd
from wordcloud_cn import generate_cn_word_cloud

df = pd.read_csv('./reviews/Mainland_China/reviews_Mainland_China_2019_10_27.csv')

title_series = " / ".join(df.title)
generate_cn_word_cloud(title_series)

title_review = " / ".join(df.review)
generate_cn_word_cloud(title_review)