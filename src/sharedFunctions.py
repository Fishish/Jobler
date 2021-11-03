import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def retriveJobs(url, pattern):

    page = urlopen(url)
    html = page.read().decode("utf-8")
    return re.findall(pattern, html)

def checkList(keyword, jobList):
    checkedList = []
    for j in jobList:
        if keyword in j:
            checkedList.append(j)
    return checkedList

