from sharedFunctions import retriveJobs, checkList

url = "https://careers.blizzard.com/global/en/search-results?keywords=Test"
pattern = ",\"title\":\"(.*?)\",\"multi_location_array\""

jobList = retriveJobs(url, pattern)
jobList = checkList("Test", jobList)

print(jobList)

