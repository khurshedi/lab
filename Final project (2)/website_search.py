from bs4 import BeautifulSoup
import requests
from csv import writer
import webbrowser
import pyautogui as py
import time


url = "https://megasaver.com/collections/apple"

page = requests.get(url)

#for checking the link
    #print(page)

soup = BeautifulSoup(page.content, 'html.parser')

# for pulling the html code of the site
    #print (soup)

lists = soup.find_all('div', class_="product-item__info")


#print (lists)

with open('phones.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Model_storage_and_carrier', 'Price']
    thewriter.writerow(header)

    for list in lists:
        #title = list.find('div', class_="product-item product-item--vertical  1/3--tablet-and-up 1/3--desk")

        #Brand = list.find('a', class_="product-item__vendor link").text.replace('\n', '')
        Model= list.find('a', class_="product-item__title text--strong link").text.replace('\n', '')
        Price = list.find('span', class_="price price--highlight").text.replace('\n', '')
        info = [Model, Price]
        thewriter.writerow(info)

#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
#webbrowser.get(chrome_path).open(url)


#This will open a browser
webbrowser.open("https://www.google.com")
time.sleep (1)
#This sleep will make the computer to wait 3 seconds
py.write ("megasaver.com", interval=0.1)
#This py.write will enter that text into google search box
py.keyDown ('return')
# This will press the enter
py.moveTo(0, 500)
# This will move your move to a mentioned position
time.sleep(1)
# It makes the computer to wait 1 second
py.click()
# Mouse button will be pressed
py.keyDown("tab")
# Tab button will be pressed
py.keyDown ('return')

webbrowser.open("https://megasaver.com/collections/apple")

