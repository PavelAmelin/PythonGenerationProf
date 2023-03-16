# Write a program that prints all the news of a given
# category, arranging them in ascending order of confidence.

from sys import stdin

all_news = [news.strip().split(' / ') if '/' in news else news for news in stdin]
categ = all_news[-1]
news_categ = list(filter(lambda x: x[1] == categ, all_news[:-1]))
for row in sorted(news_categ, key=lambda x: (x[2], x[0])):
    print(row[0])
