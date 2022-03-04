# (1) Pull text from website
# (2) Write to a file
# Used this tutorial: https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
import requests # get website
from bs4 import BeautifulSoup # parse 
import os.path # get path for file

# URL for David Foster Wallace piece 
url = "https://fs.blog/david-foster-wallace-this-is-water/"
page = requests.get(url) 

print("Status code: {}".format(page.status_code))
# page.content is garble and we need to make it pretty 
soup = BeautifulSoup(page.content, 'html.parser')
# list(soup.children)[2] # get tags
speech = soup.find_all('blockquote')[0].get_text() # we found the tag that has the speech 

# Write to file 
f = open('davidfosterwallace', 'w')
f.write(speech) # os.path.realpath(__file__)
f.close()