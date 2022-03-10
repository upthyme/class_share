'''
A hacky script to get text for my stack (cue: forgetting C-C C-V exists)
(1) Pull text from website
(2) Write to a file
Extras: 
    - Menu with Borg friend
    - Code duplication with web scraping and example (argh!)
Resources: 
    - https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
    - https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp 
Thanks to ASCII Art Collective: 
    - https://www.asciiart.eu/electronics/robots 
''' 
import requests, os.path, time, platform, random  # get website, get paths, get time, get OS
from bs4 import BeautifulSoup # parse 

borg = """
     ,     ,
    (\____/)
     (_oo_)
       (O)
     __||__    \)
  []/______\[] /
  / \______/ \/
 /    /__\
(\   /____\
"""

def borg_print(string):
    ''' Borg is angsty and chooses to cap some letters due to an undiagnosed illness
    Some say that its because he was in Beta Kappa Gamma in college...
    '''
    newstring = ""
    rando = random.randint(1,3)
    for char in string: 
        if rando in [1,2] and char.isalpha():
            newstring += char.upper()
        else: 
          newstring += char.lower()
        rando = random.randint(1,3)
    print(newstring)

def print_menu():
    """ Prints menu to screen
    """
    print("""
    1. Scrap raw website
    2. Scrap David Foster Wallace
    3. Quit
    """)

def write_to_file(filename,text):
    """ Given a filename, we write the text to it.
    File written to where script is by default
    If a duplicate filename exists, we append timestamp 
    """ 
    directory = os.path.dirname(__file__) # place result in directory where script lives 
    if platform.system() == 'Windows':
        separator = "\\"
    separator = "/"
    newfile = (separator.join([directory,filename]))
    if os.path.exists(newfile):
        newfile += "_".join(["",str(int(time.time()))]) # append with datastamp        
    with open(newfile, 'w') as f:
        f.write(text)
    print(f"File {newfile} made")

def scrap_website():
    ''' Scrap a user provided website 
    ''' 
    borg_print("...Web scraping needs more information...")
    website = input("URL to web scrape: ") 
    newfile = input("Filename to Save As: ")
    page = requests.get(website)
    borg_print("Status code: {}".format(page.status_code))
    if page.status_code == 200: 
        content = BeautifulSoup(page.content, "html.parser")
        write_to_file(newfile, content.prettify())
        borg_print(f"I wrote the contents of {website} to {newfile}")
    else: 
        borg_print("Error: HTTP status returned NOT okay")

def scraping_example():
    ''' Scraping David Foster Wallace
    '''  
    borg_print("...Web scraping an article from David Foster Wallace")
    url = "https://fs.blog/david-foster-wallace-this-is-water/"     # URL for David Foster Wallace piece 
    filename = "davidfosterwallace"
    page = requests.get(url) 
    borg_print("Status code: {}".format(page.status_code))
    if page.status_code == 200: 
        soup = BeautifulSoup(page.content, 'html.parser') # page.content is garble and we need to make it pretty 
        speech = soup.find_all('blockquote')[0].get_text() # we luckily found the tag that has the speech 
        write_to_file(filename, speech)
        borg_print(f"I've written file:{filename} with his speech. Im good at processing.")
    else: 
        borg_print("Error: HTTP status returned NOT okay")

if __name__ == "__main__":
    print(f'''
    Welcome to the pull text program!
    Borg is happy to pull text from your computer nethers.
    {borg}
    ''') 
    menu = True 
    while menu:
        print_menu()
        choice = input("Enter: ")
        if choice == "1": # scrap random website
            scrap_website()
        elif choice == "2": 
            scraping_example()
        elif choice == "3": 
            borg_print(f"Borg says goodbye")
            quit()
        else: 
            borg_print(f"Borg confused by {choice}") 
