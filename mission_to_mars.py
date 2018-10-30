
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


# In[17]:

def scrape(): 
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    url = "https://mars.nasa.gov/news/"


    # In[4]:


    # Retrieve page with the requests module
    response = requests.get(url)


    # In[6]:


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'lxml')


    # In[7]:


    # results are returned as an iterable list
    results = soup.find('div', class_="content_title")


    # In[9]:


    news_t = results.a.text
    print(news_t)    


    # In[10]:


    results2 = soup.find('div', class_="image_and_description_container")


    # In[13]:


    news_p= results.find('div',class_="rollover_description_inner").text
    print(news_p)


    # In[18]:


    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)


    # In[25]:


    html = browser.html
    soup = bs(html, 'html.parser')

    featured_img = soup.find('img', class_='fancybox-image')

    featured_img_url = str(featured_img['src'])
    print(featured_img_url)


    # In[189]:


    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(tweet_url)


    # In[190]:


    #html = browser.html
    soup = bs(response.text, 'html.parser')

    mars_weather = soup.find('div', class_='js-tweet-text-container').p.text
    print(mars_weather)


    # In[177]:


    tables = pd.read_html(facts_url)
    tables


    # In[183]:


    df = tables[0]
    df.columns = ['parameter','value']
    df


    # In[184]:


    df.set_index('parameter', inplace=True)
    df.head()


    # In[187]:


    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    html_table


    # In[27]:


    hemisphere_image_urls = [{}]


    # In[28]:


    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    hemisphere_url_cer = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    hemisphere_url_schi = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    hemisphere_url_syr = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    hemisphere_url_val = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"


    # In[30]:


    response = requests.get(hemisphere_url)
    soup = bs(response.text, 'lxml')

    items= soup.find_all('div', class_='item')
    titles =[]

    for item in items:
        title = item.h3.text
        title= title.replace(" Enhanced","")
        titles.append(title)


    # In[33]:


    def get_imge_url(url):
        response = requests.get(url)
        soup = bs(response.text, 'lxml')

        img1= soup.find('img', class_='wide-image')
        url1 = img1['src']
    
        return url1


    # In[34]:



    urls = []
    urls.append(f"https://astrogeology.usgs.gov{get_imge_url(hemisphere_url_cer)}")
    urls.append(f"https://astrogeology.usgs.gov{get_imge_url(hemisphere_url_schi)}")
    urls.append(f"https://astrogeology.usgs.gov{get_imge_url(hemisphere_url_syr)}")
    urls.append(f"https://astrogeology.usgs.gov{get_imge_url(hemisphere_url_val)}")


    # In[35]:


    hemisphere_image_urls = []
    d ={}

    for k, v in zip(titles, urls):
        print(k)
        print(v)
        d = {'title':k, 'url':v}
        hemisphere_image_urls.append(d)


    # In[36]:


    print(hemisphere_image_urls)

