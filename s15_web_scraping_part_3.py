# 1 TASK: Import any libraries you think you'll need to scrape a website.
import bs4
import requests

# 2 TASK: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from
# the homepage.
link = 'http://quotes.toscrape.com/'
res = requests.get(link)
print(res.text)

# 3 TASK: Get the names of all the authors on the first page.
soup = bs4.BeautifulSoup(res.text, 'lxml')
for item in soup.select('.author'):
    print(item.text)

# 4 TASK: Create a list of all the quotes on the first page.
for item in soup.select('.text'):
    print(item.text)

# 5 TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top
# right from the home page
for item in soup.select('.tag-item'):
    print(item.text)

# 5 TASK: Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/.

base_url = 'http://quotes.toscrape.com/page/{}/'
all_authors = set()
page_still_valid = True
current_page = 1

while page_still_valid:

    # create url to scrape
    scrape_url = base_url.format(current_page)

    # obtain request
    res = requests.get(scrape_url)

    # check for last page
    if 'No quotes found!' in res.text:
        break

    # Turn into soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add authors to set
    for name in soup.select('.author'):
        all_authors.add(name.text)

    # add next page to counter
    current_page += 1

# Print all authors
print(all_authors)
