import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getHTML(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return html

def retriveJobsUrl(url, pattern):
    html = getHTML(url)
    return re.findall(pattern, html)

def retriveJobsHtml(html, pattern):
    return re.findall(pattern, html)


def checkList(keyword, jobList):
    checkedList = []
    for j in jobList:
        for k in keyword:
            if k in j:
                checkedList.append(j)
    return checkedList


def checkFrequency(jobList):
    orzJobList = {}
    for x in jobList:
        if x in orzJobList:
            orzJobList[x] += 1
        else:
            orzJobList[x] = 1

    orzJobList = sorted(orzJobList.items(), key=lambda item: item[1], reverse=True)
    return orzJobList

def checkPage(html, pattern):
    # print(re.search(pattern, url))
    # if re.search(pattern, url):
    #     return True
    # return False
    return re.search(pattern, html)


