from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

title = doc.title
para = doc.p
para.string = 'this is modified by python\' beautiful soup libraty'

print(para)