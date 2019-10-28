import pandas as pd
import matplotlib.pyplot as plt
from countries import *

country_tuples = list(eng_country_dic.items()) + list(cn_country_dic.items())
country_stat_dict = {}
for t in country_tuples:
    country_name = t[0]
    file_path = f'./reviews/{country_name}/reviews_{country_name}_2019_10_27.csv'
    df = pd.read_csv(file_path)
    country_stat_dict[country_name] = len(df)

ratings_dict = {
    'Mainland_China': 4.8,
    'Australia': 4.7,
    'HongKong': 4.7,
    'United_States': 4.7,
    'Philippines': 4.6,
    'Canada': 4.6,
    'India': 4.6,
}


def plot_reviews(series: pd.Series, path: str = None):
    plt.figure(figsize=(15, 10))
    series.sort_values(ascending=False).plot.bar(
        color=["#83ffd0", "#c69aff", "#f4e0b0", "#f467ae", "#f26464"])
    plt.xticks(rotation=50)
    plt.xlabel("District")
    plt.ylabel("Number of Reviews")
    if not path:
        plt.show()
    else:
        plt.savefig(path)


def plot_ratings(series: pd.Series, path: str = None):
    plt.figure(figsize=(15, 10))
    series.sort_values(ascending=False).plot()
    plt.xticks(rotation=50)
    plt.xlabel("District")
    plt.ylabel("App Rating")
    if not path:
        plt.show()
    else:
        plt.savefig(path)


plot_reviews(pd.Series(country_stat_dict), "./results/mostrecent/review_stat.png")
plot_ratings(pd.Series(ratings_dict), "./results/mostrecent/rating_stat.png")
