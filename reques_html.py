from requests_html import HTMLSession
from lxml.html.clean import Cleaner

session = HTMLSession()

r = session.get('https://python.org/')
# print(r.html.links)

# about = r.html.find('#about', first=True)
# print(about)
# # Clean the HTML content    
# print(about.text)

about1 = r.html.find('.tier-2')
print(about1)
# print(about1.text)
# Clean the HTML content    
# cleaner = Cleaner(style=True, scripts=True, comments=True, page_structure=True)
# cleaned_html = cleaner.clean_html(about1.html)