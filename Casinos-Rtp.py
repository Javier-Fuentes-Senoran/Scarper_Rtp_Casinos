
#######################################################################
##########Finding all casinos and their respective returns#############
#######################################################################


#Libraries and functions

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #(html slow)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

    ##OPTIONS#
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

   ##DRIVER
driver_path="F:\chromedriver.exe"

    ##WEB
driver=webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get("https://slotcatalog.com/en")
time.sleep(3)

    ##Close pop up 
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/button")))\
    .click()
time.sleep(3)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div[1]")))\
    .click()
time.sleep(3)

    #Casino Label
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div[7]/nav/ul/li[5]/a")))\
    .click()
time.sleep(5)

    #Casino RTP
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div[7]/nav/ul/li[5]/ul/li[4]/a")))\
    .click()
time.sleep(15)

    #Load More Casino (All of them)
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[4]/div/div/div/div[13]/div/a")))\
    .click()
time.sleep(3)

############CASINOS#############

Casinos=driver.find_elements(By.XPATH,'//div[@class="bonusItemContent"]/p[@class="readyToPlay"]')

List_Casinos=list()

for Casinos in Casinos:
    Casinos=Casinos.text
    Casinos=Casinos.replace("Ready to play for real at ","").replace("?","")
    List_Casinos.append(Casinos)
    
print(List_Casinos)   


#########RTP Casinos#########

RTP_Casinos=driver.find_elements(By.XPATH,'//*[@id="top_casinos_filter"]/div/div/a/p')


List_RTP_Casino=list()

for RTP_Casinos in RTP_Casinos:
    
    RTP_Casinos=RTP_Casinos.text
    
    RTP_Casinos=RTP_Casinos.replace("Casino RTP:","").replace("*","")
    
    List_RTP_Casino.append(RTP_Casinos)


#########Links Casinos#########

Links_Casinos=driver.find_elements(By.XPATH,'//div/div/div/div/div/a[contains(text(),"Casino review")]')

List_Links_Casino=list()

for Links_Casinos in Links_Casinos:
    
    Links_Casinos=Links_Casinos.get_attribute('href') 

    
    List_Links_Casino.append(Links_Casinos)


print(List_Links_Casino)


#########Data Frame about all data recolleted#########

import pandas as pd

df=pd.DataFrame({"Casinso":List_Casinos,"RTP":List_RTP_Casino, "Link":List_Links_Casino})
print(df)


df.to_csv("Casino-Rtp.csv",index=False)  #Save-csv
df.to_csv("Casino-Rtp",index=False)  #Save-notebook

driver.quit()