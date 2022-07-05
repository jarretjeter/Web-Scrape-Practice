from pprint import pprint
from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.reddit.com/r/news/comments/mzp1hg/droughthit_california_orders_nestl%C3%A9_to_stop/")

# print(result.status_code)
# print(result.headers)
# pprint(result.headers)

src = result.content
print(src)

soup = BeautifulSoup(src, features="html.parser")
links = soup.find_all("a")
# print(f"LINKS: \n{links}")
# print("\n")

for link in links:
    print(f"LINK: {link}")
    print(f"HREF: {link.attrs['href']}")