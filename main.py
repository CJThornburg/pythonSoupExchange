from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currencey):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currencey}&amount=1'
  # grabs source code
  content = requests.get(url).text
  # print(content)

  #parse source code for just info you want

  # this creates a beautiful soup object so then you can actually parse
  soup = BeautifulSoup(content, 'html.parser')
  #query through the object of what you want, and only the text not the whole element
  rate = soup.find('span', class_="ccOutputRslt").get_text()
  rate = float(rate[0:-4])
  return rate

get_currency("INR", "USD")
