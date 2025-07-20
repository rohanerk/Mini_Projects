#!python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok = True)

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)


    # FInd the URL of the comic image

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicURL = comicElem[0].get('src')
        print('Downloading image %s...' % (comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd',os.path.basename(comicURL)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        image.close()

    prevLink = soup.select('a[rel = "prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')
