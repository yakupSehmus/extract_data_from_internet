import requests
from bs4 import BeautifulSoup

url = "https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-s%C3%BCper-lig/2020-2021/482ofyysbdbeoxauk19yg7tdt"
response = requests.get(url)

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")

"""
for i in soup.find_all("a"): #sitenin html sindeki tüm a etiketlerini gösterir
    print(i.get("href")) #sitenin içinde girilebilcek linkleri gösterir eğer hrefe yerine text yazarsan linkin üstündeki isimleri görürsün
    print("*************************************************")
"""

"""
print(soup.find_all("div", {"class":"page-section-header"}))
# classı .. olan divleri gösterir
"""

#for i in soup.find_all("tr"):
#    print(i.get("data-team-name"))
for i in soup.find_all("tr"):
    print(i.text)