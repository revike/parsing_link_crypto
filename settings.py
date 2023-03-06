from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

file = 'data.json'
time_sleep = .5
url = 'https://isthiscoinascam.com/all-cryptocurrencies'

chrome_options = Options()
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"
chrome_options.add_argument('start-maximized')
driver = webdriver.Chrome(
    executable_path='./chromedriver', options=chrome_options, desired_capabilities=caps)
