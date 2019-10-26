# !/usr/bin/env python

# .getAttribute("href").replace(/\//g, "")

import time
import requests
import csv
import typing
from datetime import datetime


def is_error_response(http_response, seconds_to_sleep: float = 1) -> bool:
    """
    Returns False if status_code is 503 (system unavailable) or 200 (success),
    otherwise it will return True (failed). This function should be used
    after calling the commands requests.post() and requests.get().

    :param http_response:
        The response object returned from requests.post or requests.get.
    :param seconds_to_sleep:
        The sleep time used if the status_code is 503. This is used to not
        overwhelm the service since it is unavailable.
    """
    if http_response.status_code == 503:
        time.sleep(seconds_to_sleep)
        return False

    return http_response.status_code != 200


def get_json(url) -> typing.Union[dict, None]:
    """
    Returns json response if any. Returns None if no json found.

    :param url:
        The url go get the json from.
    """
    response = requests.get(url)
    if is_error_response(response):
        return None
    json_response = response.json()
    return json_response


def get_reviews(appID, file_lines, page=1) -> typing.List[list]:
    print(f'Requesting page {page} of appID {appID}')
    url = 'https://itunes.apple.com/rss/customerreviews/id=%s/page=%d/sortby=mostrecent/json' % (appID, page)
    data = get_json(url)
    if not data:
        return file_lines

    feed = data.get('feed')

    for entry in feed.get('entry'):
        if entry.get('im:name'): continue
        review_id = entry.get('id').get('label')
        title = entry.get('title').get('label')
        author = entry.get('author').get('name').get('label')
        author_url = entry.get('author').get('uri').get('label')
        version = entry.get('im:version').get('label')
        rating = entry.get('im:rating').get('label')
        review = entry.get('content').get('label')
        vote_count = entry.get('im:voteCount').get('label')
        csv_data = [review_id, title, author, author_url, version, rating, review, vote_count]
        file_lines.append(csv_data)

    return get_reviews(appID, file_lines, page + 1)


def append_date_and_file_type(name) -> typing.AnyStr:
    current_time = datetime.now()
    return f'{name}_{current_time.year}_{current_time.month}_{current_time.day}.csv'


lines = []
csvTitles = ['review_id', 'title', 'author', 'author_url', 'version', 'rating', 'review', 'vote_count']
lines.append(csvTitles)

content = get_reviews(1444383602, lines)

file_path = append_date_and_file_type('./reviews/reviews')
with open(file_path, 'w+') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(content)

print("done")
