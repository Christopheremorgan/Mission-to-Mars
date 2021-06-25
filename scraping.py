#!/usr/bin/env python


# Import Splinter & BeautifulSoup & ChromeDriver
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Other dependencies
import pandas as pd
import datetime as dt


def scrape_all():

    # Set up Splinter - Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)


    # call new function to assign to variables to pass to dictionary
    news_title, news_paragraph = mars_news(browser)
        

    # Run all scraping functions and store results in dictionary
    data = {
          "news_title": news_title,
          "news_paragraph": news_paragraph,
          "featured_image": featured_image(browser),
          "facts": mars_facts(),
          "last_modified": dt.datetime.now(),
          "hemispheres": hemisphere_srape(browser)}


    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)


    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')


    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None


    return news_title, news_p


def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')


    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'


    return img_url


def mars_facts():

    # Add try/except for error handling
    try:
      # use 'read_html" to scrape the facts table into a dataframe
      df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None


    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hemisphere_srape(browser):

    # Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # Initiate list to hold the images and titles.
    hemisphere_image_urls = []


    # Retrieve the image urls and titles for each hemisphere.

    for x in range(4):
        # Initialize dictionary
        hemispheres = {}
    
        # Parse the resulting html with soup
        html = browser.html
        hemi_soup = soup(html, 'html.parser')
    
        # Retrieve hemisphere titles
        title = hemi_soup.find_all('h3')[x].text
        print(title)
    
        # Automate click to hemisphere page to retrieve hemisphere images
        full_image_link = browser.find_by_tag('h3')[x]
        full_image_link.click()

        html = browser.html
        full_img_soup = soup(html, 'html.parser')
    
        img_url_rel = full_img_soup.find('img', class_='wide-image').get('src')
        img_url = f'https://marshemispheres.com/{img_url_rel}'
        print(img_url)
    
        # Build dictionary of images and titles to append to list
        hemispheres = {
            'img_url': img_url,
            'title': title
            }
        print(hemispheres)
    
        hemisphere_image_urls.append(hemispheres)

        browser.back()

    return hemisphere_image_urls

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())

