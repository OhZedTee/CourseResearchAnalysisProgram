import sys
import os
import requests
from datetime import date

# Semester variable representing which semester we are scraping
SEMESTER = 'W21'

# Pre: Header from HTTP Response is returned
# Post: Cookie in Dictionary format is returned to be used for session storage
def get_cookie_from_header(header):
    ''' Converts header cookie to dictionary and returns it'''
    cookie_dict = {}

    # get the cookie from the header and split it into its parts
    cookies = header['Set-Cookie'].split(", ")
    
    # Convert string cookie into dictionary cookie
    for cookie in cookies:
        cookie_dict[cookie.split('=')[0]] = cookie.split('=')[1]
        
    return cookie_dict


# Pre: None
# Post: Saves HTML file containing Webadvisor course data for the given semester if one doesn't exist for the current date
def scrape_to_HTML():
    '''Gets todays date and checks if we've scraped today, if not it scrapes and stores the HTML file in the data directory, finally it returns the file name'''
    #get todays date and create file name with date in format (mm-dd-yy)
    data_dir = os.getcwd()
    today = date.today().strftime("%m-%d-%y")
    check_file = data_dir + "/data/" + "Webadvisor-" + today + ".html"
    new_file = False

    #check if website was not scraped already today
    if not os.path.isfile(check_file):
        print("Getting data from Webadvisor, please wait a minute...")

        # Scraping data from Webadvisor
        get_URL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?CONSTITUENCY=WBST&type=P&pid=ST-WESTS12A&TOKENIDX='
        resp = requests.get(get_URL)
        cookie = get_cookie_from_header(resp.headers)
        get_URL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?CONSTITUENCY=WBST&type=P&pid=ST-WESTS12A&TOKENIDX=' + cookie['LASTTOKEN']
        resp = requests.get(get_URL, cookies=cookie)
        cookie = get_cookie_from_header(resp.headers)
        post_URL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?TOKENIDX=' + cookie['LASTTOKEN'] + '&SS=1&APP=ST&CONSTITUENCY=WBST'
        post_fields = {"VAR1":SEMESTER, "VAR10":"", "VAR11":"","VAR12":"", "VAR13":"", "VAR14":"", "VAR15":"", "VAR16":"", "DATE.VAR1":"", "DATE.VAR2":"", "LIST.VAR1_CONTROLLER":"LIST.VAR1", "LIST.VAR1_MEMBERS":"LIST.VAR1*LIST.VAR2*LIST.VAR3*LIST.VAR4", "LIST.VAR1_MAX":"5", "LIST.VAR2_MAX":"5", "LIST.VAR3_MAX":"5", "LIST.VAR4_MAX":"5", "LIST.VAR1_1":"", "LIST.VAR2_1":"", "LIST.VAR3_1":"", "LIST.VAR4_1":"", "LIST.VAR1_2":"", "LIST.VAR2_2":"", "LIST.VAR3_2":"", "LIST.VAR4_2":"", "LIST.VAR1_3":"", "LIST.VAR2_3":"", "LIST.VAR3_3":"", "LIST.VAR4_3":"", "LIST.VAR1_4":"", "LIST.VAR2_4":"", "LIST.VAR3_4":"", "LIST.VAR4_4":"", "LIST.VAR1_5":"", "LIST.VAR2_5":"", "LIST.VAR3_5":"", "LIST.VAR4_5":"", "VAR7":"", "VAR8":"", "VAR3":"", "VAR6":"", "VAR21":"UG", "VAR9":"", "SUBMIT_OPTIONS":""}
        course_data = requests.post(post_URL, data=post_fields, cookies=cookie)
    
        # Writing scraped data from webadvisor to a html file
        file = open(check_file,"w+")
        file.write(course_data.text)
        file.close()
        new_file = True

    # return file name
    return check_file, new_file

