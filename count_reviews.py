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

plt.figure(figsize=(15, 10))
pd.Series(country_stat_dict).sort_values(ascending=False).plot.bar(
    color=["#83ffd0", "#c69aff", "#f4e0b0", "#f467ae", "#f26464"])
plt.xticks(rotation=50)
plt.xlabel("District")
plt.ylabel("Number of Reviews")
plt.show()
# plt.savefig("./results/mostrecent/review_stat.png")
