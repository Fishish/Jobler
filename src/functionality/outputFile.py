import csv
import os
from pathlib import Path
from datetime import date


def create_data_directory():
    if not os.path.exists(os.path.expanduser("~/Documents/Jobler/Data/")):
        Path(os.path.expanduser("~/Documents/Jobler/Data/")).mkdir(parents=True, exist_ok=True)

def create_company_directory(name):
    if not os.path.exists(os.path.expanduser("~/Documents/Jobler/Data/" + name)):
        Path(os.path.expanduser("~/Documents/Jobler/Data/" + name)).mkdir(parents=True, exist_ok=True)

def get_today():
    today = date.today()
    dt_string = today.strftime("%d_%m_%Y")
    return dt_string

def create_csv_file(company, jobList, date):

    with open(
            os.path.expanduser("~/Documents") + "/Jobler/Data/" + company + "/" + date + "_" + company + ".csv",
            "w",
            newline="",
    ) as new_file:
        fieldnames = ['Job', 'Frequency']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        print("file Writing " + str(jobList))
        for job in jobList:
            writer.writerow({'Job': job[0], 'Frequency': job[1]})
        #
        #
        # csvwriter = csv.writer(new_file, delimiter=",")
        # csvwriter.writerow(["Job", "Frequency"])

