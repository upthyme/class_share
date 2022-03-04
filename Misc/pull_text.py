'''
A hacky script to get text for my stack (cue: forgetting C-C C-V exists)
(1) Pull text from website
(2) Write to a file
Resources: 
    - https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
    - https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp 
''' 
import requests, os.path, time, platform  # get website, get paths, get time, get OS 
from bs4 import BeautifulSoup # parse 

def write_to_file(filename,text):
    """ Given a filename, we write the text to it.
    If a duplicate filename exists, we append timestamp 
    """ 
    directory = os.path.dirname(__file__) # place result in directory where script lives 
    if platform.system() == 'Windows':
        separator = "\\"
    separator = "/"
    newfile = (separator.join([directory,filename]))
    if os.path.exists(newfile):
        newfile += "_".join(["",str(int(time.time()))]) # append with datastamp        
    f = open(newfile, 'w')
    f.write(text)
    f.close()

if __name__ == "__main__":
    # URL for David Foster Wallace piece 
    url = "https://fs.blog/david-foster-wallace-this-is-water/" 
    filename = "davidfosterwallace"
    page = requests.get(url) 
    print("Status code: {}".format(page.status_code))
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser') # page.content is garble and we need to make it pretty 
        # list(soup.children)[2] # get tags
        speech = soup.find_all('blockquote')[0].get_text() # we luckily found the tag that has the speech 
        write_to_file(filename, speech)
    else: 
        print("Error: HTTP status returned NOT okay")