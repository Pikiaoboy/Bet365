import csv,time,re 
from selenium import webdriver
from bs4 import BeautifulSoup,Comment

####
#Stage 1 - get to Odds Page for sport
#Set website base url
base_url = "https://bet365.com"
#sports_url = base_url+"/sports-betting"

#Set output location
base_file = "C:\\Temp\\Results\\Bet365\\"

#load browser driver
driver = webdriver.Chrome()
driver.maximize_window()
#loads 365 base page
driver.get(base_url)
#loads 365 sports page and waits for load to finish
driver.find_element_by_xpath("//a[@title='Sports Betting']").click()
time.sleep(10)

#loads Soccer page and waits for load to finish
driver.find_element_by_xpath("//div[@class='wn-Classification '][contains(.,'Soccer')]").click()
time.sleep(5)

#finds all subpage links from middle page for different leagues
elements = driver.find_elements_by_xpath("//div[starts-with(@class,'sm-CouponLink ')]")

#loads 4th link for testing (Soccer - UK List)
#TODO - Expand to cover all 365 Soccer Lists
elements[3].click()
time.sleep(5)

#finds all subpage links from middle page for different matches
#recursive testing start from here (after reloading UK List)
market_groups = driver.find_elements_by_xpath("//div[starts-with(@class,'gl-MarketGroup cm-CouponMarketGroup')]")
#loads second link for testing
market_groups[1].find_element_by_xpath(".//div[@class='sl-CouponFixtureLinkParticipant_Name ']").click()
time.sleep(3)
###ISSUE - element not visible for selenium to expand/contract option
#doesnt include gl-MarketGroup_Open
driver.find_elements_by_xpath("//div[starts-with(@class, 'gl-MarketGroupButton ')][not (contains(@class, 'gl-MarketGroup_Open'))]")
mylen = len(driver.find_elements_by_xpath("//div[starts-with(@class, 'gl-MarketGroupButton ')][not (contains(@class, 'gl-MarketGroup_Open'))]"))

for i in range (0,mylen-1):
    driver.find_element_by_xpath("//div[starts-with(@class, 'gl-MarketGroupButton ')][not (contains(@class, 'gl-MarketGroup_Open'))]").click()
    time.sleep(1)





#Stage 2 - parse odds
#loads code into soup var
soup = BeautifulSoup(driver.page_source, 'lxml')
#marketgps = soup.findAll("div", {"class": re.compile('gl-MarketGroup *')}) #class_="gl-MarketGroup*")
marketgps = soup.findAll("div",class_='gl-Participant')
len(marketgps)
