import requests
import lxml
from bs4 import BeautifulSoup


def Crawl():
    url = input("Enter a URL: ")
    fileName = input("Enter a file name: ")
    fileName = fileName + ".txt"
    f = requests.get(url)
    soup = BeautifulSoup(f.text, 'lxml')
    # find only the text in the body of the page
    # remove the html tags
    # create a text file and write the text
    newFile = open(fileName, "w")
    for text in soup.find_all('p'):
        try:
            newFile.write(text.text)
        except:
            pass
    newFile.close()
    return fileName



