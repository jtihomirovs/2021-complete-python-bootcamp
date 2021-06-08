import bs4
import requests

# result = requests.get("http://example.com")

# print(type(result))
# print(result.text)

# soup = bs4.BeautifulSoup(result.text, "lxml")
#
# print(soup)
# print(soup.select('title')[0].getText())
# print(soup.select('h1'))
# print(soup.select('p'))

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
for item in soup.select('.toctext'):
    print(item.text)

# print(soup.select('.toctext'))

res2 = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res2.text, 'lxml')
computer = soup.select('.thumbimage')[0]
print(computer['src'])

image_link = requests.get(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
# print(image_link.content)
f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()
