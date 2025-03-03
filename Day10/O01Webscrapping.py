
from bs4 import BeautifulSoup

with open("C:\Training\PycharmProjects\IBMBatch09\Day10\mypage.html", "r") as HTMLR:
    content = HTMLR.read()

    soup = BeautifulSoup(content, "lxml")

    tag = soup.find("h5")
    print(tag)
    print("-" * 60)

    crdTitle = soup.find("h5").text
    print(crdTitle)
    print("-" * 60)

    crdTitles = soup.find_all("h5")
    print(crdTitles)
    print("-" * 60)

    for ctitle in crdTitles:
        print(ctitle.text)
    print("-" * 60)

    cards = soup.find_all("div", class_="card")
    for card in cards:
        crd_title = card.h5.text
        price = card.a.text.split()[-1]

        print(f"Traning on {crd_title} will cost {price}")