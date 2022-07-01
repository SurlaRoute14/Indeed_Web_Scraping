import re
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd
import time

# Dies ist die Liste mit allen relevanten Keywords.

keywordlist = []
keywords = ["PYTHON", "JAVA", "SQL", "NOSQL", "MONGODB", "CASSANDRA",
            "AWS", "AZURE", "SPARK", "AIRFLOW", "HIVE", "HADOOP",
            "KAFKA", "TABLEAU", "EXCEL", "QLIK", "POWER-BI",
            "DYNAMODB", "WAREHOUS", "ALTERYX", "LAKE", "ETL", "CI/CD", "BASH",
            "SHELL", "GIT"]
#Warehous, da dies sowohl in Warehouse als auch Warehosusing vorhanden ist.

occurences = []
tags = []
nopa = 30

# Hier sichere ich die href Links zu jeder einzelnen Stellenanzeige in einer Liste.

for i in range(nopa):
    print(i)
    url = "https://de.indeed.com/jobs?q=Data%20Engineer&start=" + str(i)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    outer_most_point=soup.find('div',attrs={'id': 'mosaic-provider-jobcards'})
    for job in outer_most_point.find('ul'):
        point = job.find("a")
        if point is not None:
            tags.append(point["href"])
print(len(tags), "Stellenanzeigen vorhanden")

# Nun werde ich die Beschreibungen jeder dieser Stellenanzeigen mit meiner
#Keyword-Liste vergleichen und die vorkomnisse der Keywords zu zählen.
#Jedes Keyword wird pro Beschreibung nur einmal gezählt. Um einem Ban zu umgehen,
#habe ich 1 stündige Pausen nach 75 Stellenanzeigen eingebaut. Da ich das Skript
#über Nacht laufen lasse, stört mich die Laufzeit nicht.

try:

    for i in range(len(tags)):
        if i in (75,150,225,300,375):
            print("""----------------------------------------------------
Waiting to avoid ban
----------------------------------------------------""")
            time.sleep(3600)
            url_href='https://de.indeed.com' + tags[i]
            response = requests.get(url_href)
            soup2 = BeautifulSoup(response.text, 'html.parser')

            for i in soup2.find('div',{'class':'jobsearch-jobDescriptionText'}):
                if i is not None:
                    keywordsublist = []             #out
                    for keyword in keywords:
                        if keyword in str(i).upper():
                            keywordsublist.append(keyword) #original: keywordlist.append(keyword)
                keywordsublist = list(set(keywordsublist)) #out
                keywordlist = keywordlist + keywordsublist
        else:
            print("Crawling job number:", str(i+1))
            url_href='https://de.indeed.com' + tags[i]
            response = requests.get(url_href)
            soup2 = BeautifulSoup(response.text, 'html.parser')

            for i in soup2.find('div',{'class':'jobsearch-jobDescriptionText'}):
                if i is not None:
                    keywordsublist = []             #out
                    for keyword in keywords:
                        if keyword in str(i).upper():
                            keywordsublist.append(keyword) #original: keywordlist.append(keyword)
                keywordsublist = list(set(keywordsublist)) #out
                keywordlist = keywordlist + keywordsublist

    for keyword in keywords:
        if keyword in keywordlist:
            occurences.insert(keywords.index(keyword),keywordlist.count(keyword))
        else: occurences.insert(keywords.index(keyword),0)

    df = pd.DataFrame( list(zip(keywords, occurences)), columns =['Technology', 'num'])
    df = df[df.num != 0]

    df = df.sort_values('num')
    plot= plt.bar('Technology', 'num', data=df, color='coral')
    plt.ylabel('Vorkomnisse')
    plt.xlabel('Technologien')

    plt.show()

except:
    for keyword in keywords:
        if keyword in keywordlist:
            occurences.insert(keywords.index(keyword),keywordlist.count(keyword))

        else: occurences.insert(keywords.index(keyword),0)

        df = pd.DataFrame( list(zip(keywords, occurences)), columns =['Technology', 'num'])
        df = df[df.num != 0]
        df = df.sort_values('num')

        plot= plt.bar('Technology', 'num', data=df, color='coral')
        plt.set_size_inches(10, 7)
        plt.ylabel('Vorkomnisse')
        plt.xlabel('Technologien')
