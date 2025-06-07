from bs4 import BeautifulSoup

with open("file.html","r") as f:
    content = f.read()
soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.find_all("a"))
print(soup.find_all("a", href=True))
