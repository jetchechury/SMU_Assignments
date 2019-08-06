#!/usr/bin/env python
# coding: utf-8
import os
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd
import time


def init_browser():

#Executable path to driver
    executable_path={'executable_path':'/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# # NASA MARS NEWS

def scrape():
    mars_info={}

    browser=init_browser()

    # URL of page to be scraped
    url='https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(2)

    # Scrape page into Soup
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find headline and summary
    news_title=soup.find('div',class_='content_title').find('a').text
    news_p=soup.find('div',class_='article_teaser_body').text

    mars_info["news_title"]=news_title
    mars_info["news_p"]=news_p

    # Store data in a dictionary
    #mars_info={
   #     "news_title",
    #    "news_p"
   # }

    #browser.quit()
    
# # JPL MARS SPACE IMAGES

    #browser=init_browser()

    # Visit url
    jpl_mars_images_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_mars_images_url)
    time.sleep(2)
    #Scrape page into soup
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')


    #Find URL for featured image
    featured_image_url=soup.find('article')['style'].replace('background-image: url(','').replace(');','')

    #"Unpack URL" - remove ''
    featured_image_url=featured_image_url[1:-1]

    #Base URL
    jpl_url='https://www.jpl.nasa.gov'

    #Base URL + Image URL
    featured_image_url=jpl_url+featured_image_url

    #Add image URL to dictionary
    mars_info["featured_image_url"]=featured_image_url

    #Close browser after scraping
    browser.quit()

# # MARS WEATHER

    browser=init_browser()

    #Visit url
    mars_weather_twitter='https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_twitter)

    time.sleep(2)

    #Scrape into Soup
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    #Gather weather data from latest tweet
    tweets=soup.find('p',class_='TweetTextSize').text
    #Remove excess information
    mars_weather=tweets.replace('InSight','')

    #Add information to dictionary
    mars_info["mars_weather"]=mars_weather

    #Close browser after scraping
    browser.quit()

# # MARS FACTS

    browser=init_browser()

    #Visit url
    mars_facts_url='https://space-facts.com/mars/'
    
    time.sleep(2)

    #Read tables
    tables=pd.read_html(mars_facts_url)

    #Assign variable to first table
    mars_profile_df=tables[0]
    
    #Format table
    mars_profile_df.columns=['','Value']
    mars_profile_df.set_index('',inplace=True)
    mars_profile_df

    #Transform table into hml
    mars_profile=mars_profile_df.to_html()

   #Add table to dictionary
    mars_info["mars_profile"]=mars_profile

    #Close browser after scraping
    browser.quit()

# # MARS HEMISPHERES

    browser=init_browser()

    #Visit url
    mars_hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemisphere_url)

    time.sleep(2)

    #Scrape into Soup
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    #Find all information for mars hempisheres
    hemispheres=soup.find_all('div',class_='item')

    #Create empty list to store information
    hemisphere_image_url=[]

    #Loop through ifnormation found to identify image title and url
    for link in hemispheres:

        #Assign variable to title
        title=link.find('h3').text
        
        #Assign variable to link to full image page
        hemisphere_page_url=link.find('a',class_="itemLink product-item")['href']
        

        mars_hemisphere_base_url='https://astrogeology.usgs.gov'
        
        #Visit full image page
        browser.visit(mars_hemisphere_base_url+hemisphere_page_url)
        html=browser.html
        
        time.sleep(2)

        #Parse with Soup
        soup=BeautifulSoup(html,'html.parser')
        
        #Retrieve full image url
        img_url=soup.find('img',class_='wide-image')['src']
        
        #Append full image url to base url
        img_url= mars_hemisphere_base_url + img_url
        
        #Add information to hempishere list
        hemisphere_image_url.append({'title':title,'image_url':img_url})

    mars_info["hemisphere_image_url"]=hemisphere_image_url

   
    browser.quit()

    return mars_info
    





