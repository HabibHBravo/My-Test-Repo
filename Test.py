import csv

csvHeader = ["Site Name", "Distance Ring (mi)", "Population"] 
csvData = [("Ponce", 1, 2500), ("Ponce", 2, 3500), ("Ponce", 2, 3500)

with open("MyCSV","w", encoding="UTF8", newline="") as popDataCSV:
    dataWriter = 
    dataWriter.writerow(csvHeader)
    dataWriter.writerows(csvData)
