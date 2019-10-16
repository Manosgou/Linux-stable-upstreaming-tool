import os
import sys
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
    print("4. Exit")
    select = input("Select: ")

    return select


def check_current_version():
    kernel_version = []
    with open('Makefile', 'r') as f:
        for lines in f.readlines()[:3]:
            for words in lines.split()[2:3]:
                kernel_version.append(words)
    return kernel_version


def latest_version():
    url = "https://www.kernel.org"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    releases_table = soup.find(id='releases')
    versions = releases_table.findAll('strong')
    versions_table = []
    for i in versions:
        versions_table.append(i.text)

    return versions_table[3:8]


def check_for_updates():
    ccv = check_current_version()
    current= ccv[0]+"."+ ccv[1]+"."+ ccv[2]
    print("Your current linux stable version is: " + current)
    vp = ccv[0]+"."+ ccv[1]
    lv = latest_version()
    matching = [s for s in lv if vp in s]       
    if current in matching:
        print("You are up-to-date")
        t.sleep(0.5)
        sys.exit()
    else:

        print("You need to update,latest linux stable is:", matching)


def upstream():
    print("1. Update to the latest version available")
    print("1. Update to the specified version (e.g. -v 4.9.196)")
    print("3. Back")
    select = input("Select:")
    if select =='1':
        pass
    elif select =='2':
        pass
    else:
        main()

def main():
    w = welcome()
    if w == '1':
        ccv = check_current_version()
        current= ccv[0]+"."+ ccv[1]+"."+ ccv[2] 
        print("Your current linux stable version is: " + current)
        print("Further more:")
        print("VERSION = ", ccv[0])
        print("PATCHLEVEL = ", ccv[1])
        print("SUBLEVEL = ", ccv[2])
    elif w == '2':
        check_for_updates()
    elif w == '3':
        upstream()

    elif w == '4':
        print("Exiting...")
        t.sleep(0.3)
        sys.exit()
    else:
        print("You must select one of the options above")
        print("")
        print("")
        print("")
        t.sleep(1)
        main()


if __name__ == "__main__":
    main()
