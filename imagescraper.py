# IMPORTS #
import os
import requests
from bs4 import BeautifulSoup as bs

# SET VARIABLES #
url = "https://unsplash.com/search/photos/puppet"
page = requests.get(url)
soup = bs(page.text, 'html.parser')
image_tags = soup.find_all('img')
i = 0

# CREATE DIRECTORY TO STORE IMAGES #

if not os.path.exists('puppet'):
    os.makedirs('puppet')

# CHANGE TO CREATED DIRECTORY
os.chdir('puppet')

# DOWNLOAD 50 IMAGES INTO FOLDER #
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200 and i < 50:
            with open('puppet_' +str(i) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                i += 1
    except:
        pass