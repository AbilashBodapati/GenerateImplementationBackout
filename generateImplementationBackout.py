
# Import all the libraries I need
import os
import sys
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

class githubAccess:
    def construct(self, username, password):
        self.username = username
        self.password = password
        
        # Use the executable file in my desktop to start the chromedriver
        self.service = Service('/home/abilashbodapati/Desktop/chromedriver')
        # Start the chromedriver service
        self.service.start()
        # Target web-url initialized (Github login-page)
        self.driver = webdriver.Remote(self.service.service_url)

    def startChromeService(self):
        # Use the executable file in my desktop to start the chromedriver
        # service = Service('/home/abilashbodapati/Desktop/chromedriver')

        # Start the chromedriver service
        # self.service.start()

        # Target web-url initialized (Github login-page)
        # driver = webdriver.Remote(service.service_url)
        self.driver.get('http://www.github.com/login')
        # Maximize the window when the webpage is opened
        self.driver.maximize_window()

    def accessGithub(self):
        '''
            This is the point 
            I am on the Github
            login page.
        '''
        # Passing username argument into login field
        self.driver.find_elements_by_xpath("//input[@name='login']")[0].send_keys(self.username)
        # Passing password argument into password field
        self.driver.find_elements_by_xpath("//input[@name='password']")[0].send_keys(self.password)
        # Once the credentials are passed in, click on the submit button
        self.driver.find_elements_by_xpath("//input[@name='commit']")[0].click()

    def getFiles(self, repo):
        
        fileName = []
        URL = "https://github.com/AbilashBodapati/%s" %(repo)
        
        uClient = uReq(URL)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")

        job_elems = page_soup.findAll('div', {"class": "Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block"})
        
        print(job_elems)
        

        

        #return fileName

    def getContent(self, listRepo):
        self.driver.find_element_by_xpath("//div[@id='repos-container']/ul/li/div/a[@href='/AbilashBodapati/ProjectCreation']").click()
        for repo in listRepo:
            self.getFiles(repo)

        self.driver.find_element_by_xpath("//div[@role='grid'][@aria-labelledby='files']/div[3]/div[@role='rowheader']/span/a[@href='/AbilashBodapati/ProjectCreation/blob/master/CreateGitRepo.py']").click()
        time.sleep(2)
        
    def exitApplication(self):
        # Exit out of the window after the repo is created
        time.sleep(2) # Let the user actually see something!
        self.driver.quit()

class generateImplementationBackout:
    # Constructor for this class that store the command line arguments
    def __init__(self, argv):
        """
            arg[0] => RootFolder in the Project folder
            arg[1] => Username
            arg[2] => Password        
        """
        self.parent_folder_name = argv[0]
        self.username = argv[1]
        self.password = argv[2]

    # Function to create a new Directory to creat a new project
    def createNewDirectory(self):
        try:
            # Change the current working Directory
            os.chdir("/home/abilashbodapati/Desktop/Projects/")
            print("Directory changed to /Desktop/Projects")
        except OSError:
            print("Can't change the Current Working Directory")
            sys.exit()     


        try:
            # Create a new Directory
            os.mkdir(self.parent_folder_name + "/")
            print("Directory Created in /Desktop/Projects")
        except OSError:
            print("Directory already exists")
            sys.exit()

        try:
            # Change the current working Directory
            #projectPath = "/home/abilashbodapati/Desktop/Projects/%s/ " %(argv[0])
            os.chdir("/home/abilashbodapati/Desktop/Projects/" + self.parent_folder_name + "/")
            print("Directory changed to " + self.parent_folder_name + " Folder")
        except OSError:
            print("Can't change the Current Working Directory")
            sys.exit()

    # Function to create Files => README.md and file name
    def createFiles(self):
        
        # Creates the File in the project folder
        try:
            os.system("touch %s.%s" %('Implementation', 'txt'))
            os.system("touch %s.%s" %('Backout', 'txt'))
        except OSError:
            print("File Already Exists")
            sys.exit()

# Main Function
if __name__ == "__main__":

     #createProject(sys.argv[1:])
    #generateImplementationBackoutFiles = generateImplementationBackout(sys.argv[1:])
    
    #generateImplementationBackoutFiles.createNewDirectory()
    #generateImplementationBackoutFiles.createFiles()

    # Run a Separate python script to create a git repo on github
    #os.system("python3 ../PrivateFiles/CreateGitRepo.py %s" %(self.parent_folder_name))
    CreateGitRepo = githubAccess()

    CreateGitRepo.construct(sys.argv[2], sys.argv[3])
    CreateGitRepo.startChromeService()
    CreateGitRepo.accessGithub()

    CreateGitRepo.getContent(['ProjectCreation'])

    CreateGitRepo.exitApplication()

    