import csv
from selenium import webdriver
from bs4 import BeautifulSoup,Comment
import time

#Set website base url
base_url = "https://bet365.com"
#sports_url = base_url+"/sports-betting"

#Set output location
base_file = "C:\\Temp\\Results\\Bet365\\"

#load browser driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
driver.find_element_by_xpath("//a[@title='Sports Betting']").click()
time.sleep(10)
#driver.find_element_by_xpath("//a[starts-with(@class,'hm-DropDownSelections_Button ')][contains(.,'Odds')]").click()
#driver.find_element_by_xpath("//a[starts-with(@class,'hm-DropDownSelections_Item ')][contains(.,'Decimal']").click()
driver.find_element_by_xpath("//div[@class='wn-Classification '][contains(.,'Soccer')]").click()
time.sleep(5)
#elements = driver.find_elements_by_xpath("//div[@class='sm-CouponLink ']")
elements = driver.find_elements_by_xpath("//div[starts-with(@class,'sm-CouponLink ')]")
elements[3].click()

market_groups = driver.find_elements_by_xpath("//div[starts-with(@class,'gl-MarketGroup cm-CouponMarketGroup')]")
market_groups[1].find_element_by_xpath(".//div[starts-with(@class,'sl-CouponParticipantWithBookCloses')]").click()
driver.back()
