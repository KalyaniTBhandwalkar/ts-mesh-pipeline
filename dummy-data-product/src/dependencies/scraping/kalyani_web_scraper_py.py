# -*- coding: utf-8 -*-
"""Kalyani_Web_Scraper.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1su_aGZODCKC2LsJFl1Jrz3CnagukXjuE

Import the libraries
"""

from bs4 import BeautifulSoup
import requests,re
import pandas as pd
import matplotlib.pyplot as plt

class Web_Scraper:
  def __init__(self, **kwargs):
    self.config = kwargs.get("config")

    # Website url
    url="https://opentender.eu"
    req=requests.get(url)
    content=BeautifulSoup(req.content,'html.parser')
    data=content.find("ul",{'class':'portal-links'})
    links=[]
    country=[]
    tender=[]
    # Get all urls
    for dlink in data.find_all('a'):
      link=url+dlink.get('href')
      links.append(link)
    # Get the number of tenders 
    for items in data.find_all('div'):
      tenders=items.get_text()
      tender.append(tenders)
    #Get the State name
    for items in data.find_all('a'):
      countrys=items.get_text()
      country.append(countrys)
    # Create empty dataframe
    df=pd.DataFrame()
    # Add columns to dataframe
    df['URL']=links
    df['Country']=country
    df['#Tender']=tender
    # Save dataframe in csv format
    df.to_csv("Kalyani_Opentender.csv")
    tender=[]
    for i in df['#Tender']:
      i=i.replace(",","")
      if "Million" in i:
        i=i.replace("Million","")
        temp =  re.sub("\D", "",i)
        temp=int(temp)*1000000
        i=temp
        tender.append(i)
      else:
        i=int(i)
        tender.append(i)

    df['#Tender']=tender
    print("========================================================")
    print("")
    print("Tender data from 33 jurisdictions")
    print(df)
    print("")
    print("========================================================")
    print("")
    
    x=df['Country']
    y=df['#Tender']
    # Figure Size
    fig, ax = plt.subplots(figsize =(16, 9))
    # Horizontal Bar Plot
    plt.barh(x,y)
    
    plt.xlabel('Number of Tenders')
    plt.ylabel('Country')
    #ax.invert_yaxis()
    plt.title("Analysis of tender data from 33 jurisdictions",fontsize = 30)
    plt.show()

if __name__ == "__main__":
    config = {}
    obj = Web_Scraper(config = config)


