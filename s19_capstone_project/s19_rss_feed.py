# File name: rssFeed.py
# Description:  Scrape ss.com retro-cars rss entries and print them out
# Author: Juris Tihomirovs
# Date: 04-06-2021

import bs4
import feedparser

NewsFeed = feedparser.parse("https://www.ss.com/lv/transport/cars/retro-cars/rss/")

print('Number of RSS posts :', len(NewsFeed.entries))

for entry in NewsFeed.entries:
    # Parse summary using beaBeautifulSoup
    soup = bs4.BeautifulSoup(entry.summary, 'html.parser')

    # Print out attributes and values of car
    print('****')
    print('Title: ', entry.title)
    print('Link: ', entry.link)
    print('Published: ', entry.published)
    print('Image link: ', soup.a.img['src'])
    print('Make: ', soup.select('b')[0].text)
    print('Model: ', soup.select('b')[1].text)
    print('Year: ', soup.select('b')[2].text)
    print('Engine: ', soup.select('b')[3].text)
    print('Price: ', soup.select('b')[4].text)

    # Other possible keys:
    # print('Summary details: ', entry.summary_detail)
    # print('Title detail: ', entry.title_detail)
    # print('Links: ', entry.links)
    # print('Published parsed: ', entry.published_parsed)
    # print('Summary: ', entry.summary)
    print('****')
