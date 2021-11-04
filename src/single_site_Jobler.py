from src.functionality.outputFile import create_data_directory, create_company_directory, create_csv_file, get_today
from src.functionality.sharedFunctions import checkList, checkFrequency, checkPage, retriveJobsUrl, getHTML, retriveJobsHtml

keyWords = ["Test", "Quality"]

rawjobs = retriveJobsUrl("https://careers.activision.com/search-results", ",\"title\":\"(.*?)\",\"multi_location_array\"")
unsortedjobs = checkList(keyWords, rawjobs)
tempList = checkFrequency(unsortedjobs)

print(tempList)