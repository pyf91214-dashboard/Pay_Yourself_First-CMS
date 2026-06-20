import re
from bs4 import BeautifulSoup
html = open('admin-cms.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('button', {'@click': lambda x: x and 'cmsTab' in x})
for l in links:
    print(l.get('@click'))
