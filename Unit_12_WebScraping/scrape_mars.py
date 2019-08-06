#!/usr/bin/env python
# coding: utf-8
import os
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time
import datetime as dt



def init_browser():

    # Initiate headless driver for deployment
    executable_path={'executable_path':'/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=True)


# # NASA MARS NEWS

def scrape_all():

    browser=init_browser()

    # URL of page to be scraped
    url='https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(2)
    # Get first list item and wait half a second if not immediately present
    browser.is_element_present_by_css("ul.item_list li.slide")

    # Scrape page into Soup
    html=browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")

        # Find headline and summary
        news_title=slide_elem.find('div',class_='content_title').find('a').text
        news_p=slide_elem.find('div',class_='article_teaser_body').text

    except AttributeError:
        return None, None
    
# # JPL MARS SPACE IMAGES
    # Visit url
    jpl_mars_images_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_mars_images_url)
    time.sleep(2)

    #Scrape page into soup
    html=browser.html
    img_soup=BeautifulSoup(html,'html.parser')

    try:
        #Find URL for featured image
        featured_image_url=img_soup.find('article')['style'].replace('background-image: url(','').replace(');','')

        #"Unpack URL" - remove ''
        featured_image_url=featured_image_url[1:-1]

        #Base URL
        jpl_url='https://www.jpl.nasa.gov'

        #Base URL + Image URL
        featured_image_url=jpl_url+featured_image_url

    except AttributeError:
        return None


# # MARS WEATHER

    #Visit url
    mars_weather_twitter='https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_twitter)

    time.sleep(2)

    #Scrape into Soup
    html=browser.html
    weather_soup=BeautifulSoup(html,'html.parser')

    #Gather weather data from latest tweet
    tweets=weather_soup.find('p',class_='TweetTextSize').text
    #Remove excess information
    mars_weather=tweets.replace('InSight','')


# # MARS FACTS

    #Visit url
    mars_facts_url='https://space-facts.com/mars/'

    time.sleep(2)
    try:
        #Read tables
        table=pd.read_html(mars_facts_url)[0]
    except BaseException:
        print(None)

    #Format table
    table.drop(['Earth'], axis=1,inplace=True)
    table.columns=['Description','Value']
    table.set_index('Description',inplace=True)

    # Transform table into html
    mars_facts= table.to_html(classes='table-striped')

# # MARS HEMISPHERES

    mars_hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(mars_hemisphere_url)

    time.sleep(2)

    hemisphere_image_urls = []

    for i in range(4):
        
        browser.find_by_css("a.product-item h3")[i].click()
        
        try:
            html=browser.html
            hemi_soup = BeautifulSoup(html, "html.parser")

            #Assign variable to title
            title=hemi_soup.find('h2',class_='title').text

            #Retrieve full image url
            relative_path=hemi_soup.find('img',class_='wide-image')['src']
            img_url='https://astrogeology.usgs.gov' + relative_path
            #Add information to hempishere list
            hemisphere_image_urls.append({'title':title,'image_url':img_url})

            browser.back()
            
        except AttributeError:
            title= None
            img_url = None
            
# def scrape_hemisphere(html_text):

#     # Soupify the html text
#     hemi_soup = BeautifulSoup(html_text, "html.parser")

#     # Try to get href and text except if error.
#     try:
#         title_elem = hemi_soup.find("h2", class_="title").get_text()
#         sample_elem = hemi_soup.find("a", text="Sample").get("href")

#     except AttributeError:

#         # Image error returns None for better front-end handling
#         title_elem = None
#         sample_elem = None

#     hemisphere = {
#         "title": title_elem,
#         "img_url": sample_elem
#     }

#     return hemisphere

# def hemispheres(browser):

#     # A way to break up long strings
#     url = (
#         "https://astrogeology.usgs.gov/search/"
#         "results?q=hemisphere+enhanced&k1=target&v1=Mars"
#     )

#     browser.visit(url)

#     # Click the link, find the sample anchor, return the href
#     hemisphere_image_urls = []
#     for i in range(4):

#         # Find the elements on each loop to avoid a stale element exception
#         browser.find_by_css("a.product-item h3")[i].click()

#         hemi_data = scrape_hemisphere(browser.html)

#         # Append hemisphere object to list
#         hemisphere_image_urls.append(hemi_data)

#         # Finally, we navigate backwards
#         browser.back()

#     return hemisphere_image_urls


    # Store in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image_url,
        "hemispheres": hemisphere_image_urls,
        "weather": mars_weather,
        "facts": mars_facts,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data




