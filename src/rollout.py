import csv

from src.functionality.sharedFunctions import  checkList, checkFrequency

studioList = {"Blizzard" : "https://careers.blizzard.com/global/en/search-results?keywords=Test",
              "Activision" : "https://careers.activision.com/search-results"
              }
patternList = {"Blizzard" : ",\"title\":\"(.*?)\",\"multi_location_array\"",
              "Activision" : "https://careers.activision.com/search-results"
              }




def run():
    jobList = retriveJobs("https://careers.activision.com/search-results", ",\"title\":\"(.*?)\",\"multi_location_array\"")
    jobList = checkList("Test", jobList)
    jobList = checkFrequency(jobList)
    print(jobList)
#<td class="search-results-column-left" title="Development Manager">Development Manager</td>

#run()
# html = getHTML("https://ea.gr8people.com/jobs?locale=en&page=1")
# #print(re.findall("<td class=\"search-results-column-left\" title=\"(.*?)\">", html))
#
# #print(html)
# if re.search("\"alert alert-error empty-text \"", html) :
#     print(html)

with open('data/countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerow("a")