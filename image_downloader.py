### This function downloads all jpgs from a given website's body into a specified directory on your computer.

import os
import re
import urllib.request

def image_list(url):
    '''This function accepts a URL and returns a list of all the links to the images on that website.'''
    web_page = urllib.request.urlopen(url)
    contents = web_page.read() .decode(errors="replace")
    web_page.close()

    body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)
    links = re.findall('(?<=src=").+?(?=")', body[0], re.DOTALL)

    final = [link for link in links if ('http' in link) and (('.jpg' in link) or ('.JPG' in link) or ('.jpeg' in link) or ('.JPEG' in link) or ('.png' in link) or ('.PNG' in link))]

    return final


def checkUrl(url):
    '''This checks to see if a website exists or not. Returns True or False'''
    try:
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        urllib.request.urlopen(request)
        return True
    except:
        return False


#main:

while True:
    url = str(input('\nPlease enter a website with pictures on it. I will download all the pictures: (or type STOP) '))
    if url.upper() == 'STOP':
        break
    directory = str(input('Which directory do you want these pictures in? '))

    #checking to make sure it is a valid url and a valid directory:
    if (checkUrl(url) and os.path.isdir(directory)):
        os.chdir(directory)

        # getting the list of image links
        jpglinks = image_list(url)

        # downloading each image and keeping the original name of the uploaded image
        for link in jpglinks:
            urllib.request.urlretrieve(link, os.path.basename(link))
        print('Finished Task!')
    else:
        print('Invalid entry.') 