# Mission-to-Mars

## Project Overview
Designed for Mars enthusiasts, a web page was created that, with a push of a button, pulls in the latest Mars news and images along with reference stats and images.  Several tools were used to build this Mars 'dashboard'...

- Python Splinter and BeautifulSoup packages were used to automate the web browser to scrape information from 4 different websites
- MongoDB was used as a NoSQL database was required to store the unstructured scraped data
- Flask was used to render data and images in a web application
- Bootstrap was used to give the web application a more polished look

## Results of the Scrape
The Mars dashboard was designed to be readable while zooming out to see the full page on a desktop.  The dashboard is also mobile responsive.  Below the image of the full desktop dashboard is an image of the mobile responsive view on an iPhone X.

MARS DESKTOP DASHBOARD

![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/mars_dash_desktop.png)


MARS MOBILE DASHBOARD

![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/mars_dash_mobile.png)


## Recent Landing Page Revisions
Three recent adjustments were made to the Mars Dashboard for a cleaner look on both desktop and mobile devices.

### News Module Updates
The news module of the dashboard was originally left justified and looked 'lost' on a mostly centered page.  Header lines were added to encase and bring attention to the latest news which is now centered.
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/News_img_old.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/news_code_old.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/news_img_new.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/news_code_new.png)

### Mars Facts Table Adjustments
The 'Mars Facts' section was adjusted to provide a more minimalist look and align better with the 'Featured Mars Image' section. The heading for facts was put at same header level as all other headers on the page.  The table border was removed for a more minimalist look and condensed to better align with the feature image.
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/facts_table_old.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/facts_table_new.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/tabel_pycode_new.png)

### Mars Hemisphere Thumbnail Images
The Mars Hemisphere images were originally larger and took up more screen space.  For a cleaner dashboard look the images were scaled down, which also allows the user to zoom out to see the entire page without having to strain the eyes.  This was the easiest change as it only required changing the column sizes.
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/hemi_images_old.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/hemi_images_new.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/hemi_code_old.png)
![image_name](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/resources/hemi_code_new.png)

## Links to Coding Files

[Mission_to_Mars.ipynb](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/Mission_to_Mars.ipynb) 

[app.py](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/app.py) 

[scraping.py](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/scraping.py) 

[index.html](https://github.com/Christopheremorgan/Mission-to-Mars/blob/main/templates/index.html) 
