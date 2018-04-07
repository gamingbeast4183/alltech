import os
os.system("sudo pip install --upgrade beautifulsoup4")
from bs4 import BeautifulSoup as BS
html = input("HTML file? \t")
f = open(html,"r+")
soup = BS(f.read(), "html.parser")
f.seek(0,0)
f.write(soup.prettify())
f.close()
