# Goal: Get title of every book with a 2 star rating
import bs4
import requests

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select('.product_pod')
example = products[0]

# We can check if something is 2 stars (string call in, example.select(rating)
# 1 - Quick and dirty way
print('star-rating Three' in str(example))

# 2 - is this class present?
# example.select(".star-rating.Three")

# example.select('a')[1]['title'] to grab the book title
# example.select('a')[1]['title']

two_star_titles = []
for n in range(1, 51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # select book html container with class .product_pod
    books = soup.select('.product_pod')

    for book in books:
        # if 'star-rating Two' in str(book)
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
