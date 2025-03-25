from selenium import webdriver
from selenium.webdriver.chrome.service import Service

'''
- inisialisasi path chrome driver
'''
PATH = "C:\\Webdriver\chromedriver.exe" 
service = Service(PATH)

'''
- insisialisasi url untuk web yang hendak di tes
- driver.tittle untuk debug 
'''
driver = webdriver.Chrome(service=service)
driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()
