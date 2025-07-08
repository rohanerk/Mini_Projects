# 1st Version
import webbrowser

fo = open("C:\\Users\\rohan\\Desktop\\cat-bounce.com.txt")
links = fo.readlines()

for i in range(len(links)):
    webbrowser.open(links[i])
  


# 2nd Version (Without indexing)

import webbrowser

fo = open("C:\\Users\\rohan\\Desktop\\cat-bounce.com.txt")
links = fo.readlines()

for link in links:
    webbrowser.open(link)
