
# Import all the libraries I need
import os
import sys
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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
    generateImplementationBackoutFiles = generateImplementationBackout(sys.argv[1:])
    
    generateImplementationBackoutFiles.createNewDirectory()
    generateImplementationBackoutFiles.createFiles()

    # Run a Separate python script to create a git repo on github
    #os.system("python3 ../PrivateFiles/CreateGitRepo.py %s" %(self.parent_folder_name))
    CreateGitRepo = githubAccess()

    CreateGitRepo.construct(sys.argv[2], sys.argv[3])
    CreateGitRepo.startChromeService()
    CreateGitRepo.accessGithub()