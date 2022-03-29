import requests
from bs4 import BeautifulSoup

city = str(input("Enter the city name: "))

url = "https://www.google.com/search?q=" + city + "+weather"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

temp = soup.find("div", attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

print("The temperature in " + city + " is " + temp + " degrees")