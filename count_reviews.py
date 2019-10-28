import pandas as pd
import matplotlib.pyplot as plt
from countries import *

country_tuples = list(eng_country_dic.items()) + list(cn_country_dic.items())

# for x axis tick display
abbreviation = {
    'Mainland_China': "CN",
    'Australia': "AU",
    'HongKong': "HK",
    'United_States': "US",
    'Philippines': "PH",
    'Canada': "CA",
    'India': "IN",
}

country_stat_dict = {}
country_mean_rating = {}
total_ratings_dict = {
    'Mainland_China': 4.8,
    'Australia': 4.7,
    'HongKong': 4.7,
    'United_States': 4.7,
    'Philippines': 4.6,
    'Canada': 4.6,
    'India': 4.6,
}
lines = []
columns = ["country", "recent rating mean", "version range", "# collected reviews"]
for t in country_tuples:
    country_name = t[0]
    file_path = f'./reviews/{country_name}/reviews_{country_name}_2019_10_27.csv'
    df = pd.read_csv(file_path)
    abbr = abbreviation[country_name]
    country_stat_dict[abbr] = len(df)
    country_mean_rating[abbr] = df.rating.mean()
    lines.append([abbr, df.rating.mean(), f'{df.version.min()}-{df.version.max()}', len(df)])

df = pd.DataFrame(lines, columns=columns)
df.to_csv("./results/review_stat.csv", index=False)


def plot_reviews(series: pd.Series, path: str = None):
    plt.figure(figsize=(15, 10))
    ax = series.sort_values(ascending=False).plot.bar()
    plt.tick_params(axis='both', which='major', labelsize=30)
    plt.xticks(rotation=0)
    plt.xlabel("District", fontsize=40)
    plt.grid(axis='y')
    plt.ylabel("Number of Reviews", fontsize=40)
    if not path:
        plt.show()
    else:
        plt.savefig(path)


def plot_ratings(series: pd.Series, path: str = None):
    plt.figure(figsize=(15, 10))
    series.sort_values(ascending=False).plot()
    plt.tick_params(axis='both', which='major', labelsize=30)
    plt.xticks(rotation=0)
    plt.xlabel("District", fontsize=40)
    plt.ylabel("Average App Rating", fontsize=40)
    if not path:
        plt.show()
    else:
        plt.savefig(path)


plot_reviews(pd.Series(country_stat_dict), "./results/review_stat.png")
plot_ratings(pd.Series(country_mean_rating), "./results/rating_stat.png")
