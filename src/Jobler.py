from src.functionality.outputFile import create_data_directory, create_company_directory, create_csv_file, get_today
from src.functionality.sharedFunctions import checkList, checkFrequency, checkPage, retriveJobsUrl, getHTML, retriveJobsHtml

studioList = {
                "Blizzard" : "https://careers.blizzard.com/global/en/search-results?keywords=Test",
                "Activision" : "https://careers.activision.com/search-results",
                "EA" : "https://ea.gr8people.com/jobs?locale=en&page="
              }
patternList = {
                "Blizzard" : ",\"title\":\"(.*?)\",\"multi_location_array\"",
                "Activision" : ",\"title\":\"(.*?)\",\"multi_location_array\"",
                "EA" : "<td class=\"search-results-column-left\" title=\"(.*?)\">"
              }
pageCheckList = {
                "Blizzard" : 0,
                "Activision" : 0,
                "EA" : "\"alert alert-error empty-text \""
              }
keyWords = ["Test", "Quality"]

def initialize():
    create_data_directory()
    for c in pageCheckList:
        create_company_directory(c)


def run():
    today = get_today()
    jobList = {}
    for s in studioList:
        if pageCheckList[s] == 0:
            rawjobs = retriveJobsUrl(studioList[s], patternList[s])
            unsortedjobs = checkList(keyWords, rawjobs)
            tempList = checkFrequency(unsortedjobs)
            jobList[s] = tempList
        else:
            i = 1
            totalList = []
            tempHtml = getHTML(studioList[s] + str(i))
            while not checkPage(tempHtml, pageCheckList[s]):
                rawjobs = retriveJobsHtml(tempHtml, patternList[s])
                totalList += rawjobs
                print(i)
                i += 1
                tempHtml = getHTML(studioList[s] + str(i))
            unsortedjobs = checkList(keyWords, totalList)
            tempList = checkFrequency(unsortedjobs)
            jobList[s] = tempList
        create_csv_file(s, jobList[s], today)


initialize()
run()
