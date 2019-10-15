import os
import requests
import time as t
from bs4 import BeautifulSoup



def welcome():
    print("Linux-stable upstreaming tool")
    print("")
    print("==========Options==========")
    print("1. Check current version")
    print("2. Check for updates")
    print("3. Upstream!(updade)")
    select = input("Select: ")

    return select
 


def check_current_version():
    kernel_version =[]
    with open('Makefile','r') as f:
        for lines in f.readlines()[:3]:        
            for words in lines.split()[2:3]:
                kernel_version.append(words) 
    return kernel_version
    
    

def latest_version():
    url = "https://www.kernel.org"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    releases_table = soup.find(id ='releases')
    versions = releases_table.findAll('strong')
    online_versions=[]
    for i in versions:
        online_versions.append(i.text)
    
    
    return online_versions[3:8]
                   
            

    
def check_for_updates():
    vps =check_current_version()
    print("Your current linux stable version is: ",vps)        
    clv=vps[0]+"."+vps[1]
    print
    ov= latest_version()
    matching = [s for s in ov if clv in s]
    print("Latest linux stable version is:",matching)
    
    
    


def upstream():
    print("Under construction.....")   
    
    


def main():
    w =welcome()
    if w=='1':
        ccv= check_current_version()
        print("Your current linux stable version is: ",ccv)
        print("Further more:")
        print("VERSION = ",ccv[0])
        print("PATCHLEVEL = ",ccv[1])
        print("SUBLEVEL = ",ccv[2])
    elif w=='2':
        check_for_updates()
    elif w=='3':
        upstream()
    else:
        print("You must select one of the options above")
        print("")
        print("")
        print("")
        t.sleep(1)
        main()
if __name__ == "__main__":
    main()








