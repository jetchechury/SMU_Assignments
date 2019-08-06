#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd


# In[2]:


get_ipython().system('which chromedriver')


# In[39]:


#Executable path to driver
executable_path={'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA MARS NEWS

# In[4]:


# URL of page to be scraped
url='https://mars.nasa.gov/news/'

# Retrieve page with the requests module
browser.visit(url)


# In[5]:



html=browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


news_title=soup.find('div',class_='content_title').find('a').text
news_p=soup.find('div',class_='article_teaser_body').text
print(news_title)
print(news_p)


# # JPL MARS SPACE IMAGES

# In[7]:


#Executable path to driver
#executable_path={'executable_path':'/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


jpl_mars_images_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_mars_images_url)


# In[9]:


html=browser.html
soup=BeautifulSoup(html,'html.parser')


# In[10]:


#Find URL for featured image
featured_image_url=soup.find('article')['style'].replace('background-image: url(','').replace(');','')

#"Unpack URL" - remove ''
featured_image_url=featured_image_url[1:-1]

#Base URL
jpl_url='https://www.jpl.nasa.gov'

#Base URL + Image URL
featured_image_url=jpl_url+featured_image_url


# In[11]:


print(featured_image_url)


# # MARS WEATHER

# In[12]:


mars_weather_twitter='https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_twitter)


# In[13]:


html=browser.html
soup=BeautifulSoup(html,'html.parser')


# In[14]:


tweets=soup.find('p',class_='TweetTextSize').text


# In[15]:


mars_weather=tweets.replace('InSight','').replace('pic.twitter.com/0KZXlbiuXO','')


# In[16]:


mars_weather


# # MARS FACTS

# In[17]:


mars_facts_url='https://space-facts.com/mars/'
tables=pd.read_html(mars_facts_url)
tables
mars_profile_df=tables[0]
mars_profile_df


# In[18]:


mars_profile_df.columns=['','Value']
mars_profile_df.set_index('',inplace=True)
mars_profile_df


# In[19]:


mars_profile_df.to_html()


# # MARS HEMISPHERES

# In[44]:


mars_hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(mars_hemisphere_url)


# In[45]:


html=browser.html
soup=BeautifulSoup(html,'html.parser')


# In[46]:


hemispheres=soup.find_all('div',class_='item')

hemisphere_image_url=[]

for link in hemispheres:
    title=link.find('h3').text
    
    hemisphere_page_url=link.find('a',class_="itemLink product-item")['href']
    
    mars_hemisphere_base_url='https://astrogeology.usgs.gov'
    
    browser.visit(mars_hemisphere_base_url+hemisphere_page_url)
    html=browser.html
    
    soup=BeautifulSoup(html,'html.parser')
    
    img_url=soup.find('img',class_='wide-image')['src']
    
    img_url= mars_hemisphere_base_url + img_url
    
    hemisphere_image_url.append({'title':title,'image_url':img_url})
    
hemisphere_image_url


# In[ ]:




