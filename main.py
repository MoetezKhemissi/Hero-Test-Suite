
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from config import default_wait_time,env
from data import Languague,FeedUrlVariations,BaseProdUrl,BaseStagingUrl
from selenium.webdriver.support.ui import Select




#------------------------Helpers-----------------------------------

def action_click(driver,element):
    action = ActionChains(driver)
    action.click(on_element = element)
    action.perform()
def explicit_wait_xpath(driver,xpath_string):
    return WebDriverWait(driver, default_wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath_string)))
def explicit_wait_presence_xpath(driver,xpath_string):
    return WebDriverWait(driver, default_wait_time).until(EC.presence_of_element_located((By.XPATH, xpath_string)))







#------------------------Navigation-----------------------------------
def test_Register_basic():
    driver=start_driver_chrome()
    firstname="moetez"
    lastname="khemissi"
    #need to change email until request to delete old
    email="khemissimoetez153@gmail.com"
    phone="+21655602457"
    password="Hero@123"
    if env=="staging":
        driver.get(BaseStagingUrl)
    else:
        driver.get(BaseProdUrl)
    joinButton=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[3]/div/button")
    action_click(driver,joinButton)
    continueWithEmail=explicit_wait_xpath(driver,"/html/body/div[1]/div[6]/div/div/div/div/div/div[1]/div/button[3]")
    action_click(driver,continueWithEmail)
    driver.find_element(By.ID, "firstname").click()
    driver.find_element(By.ID, "firstname").send_keys(firstname)
    time.sleep(0.5)
    driver.find_element(By.ID, "lastname").click()
    driver.find_element(By.ID, "lastname").send_keys(lastname)
    time.sleep(0.5)
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys(email)
    time.sleep(0.5)
    driver.find_element(By.ID, "whatsapp").click()
    driver.find_element(By.ID, "whatsapp").send_keys(phone)
    time.sleep(0.5)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(0.5)
    driver.find_element(By.ID, "confirmPassword").click()
    driver.find_element(By.ID, "confirmPassword").send_keys(password)
    time.sleep(0.5)
    agreeTOS=explicit_wait_xpath(driver,"/html/body/div[1]/div[6]/div/div/div/div/div/div[1]/div/form/div[7]/label/input")
    action_click(driver,agreeTOS)
    confirmRegistration=explicit_wait_xpath(driver,"/html/body/div[1]/div[6]/div/div/div/div/div/div[1]/div/form/button")
    action_click(driver,confirmRegistration)
    #check if referral tab is loaded TODO better tests incoming
    referraltab = explicit_wait_presence_xpath(driver,"/html/body/div/main/div/div[3]/div[3]/p")
    time.sleep(3)
    assert driver.current_url in FeedUrlVariations



def test_Login():
    email="khemissimoetez@gmail.com"
    password="Hero@123"
    driver=start_driver_chrome()
    if env=="staging":
        driver.get(BaseStagingUrl)
    else:
        driver.get(BaseProdUrl)
    joinButton=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[3]/div/button")
    action_click(driver,joinButton)
    loginTab = explicit_wait_xpath(driver,"/html/body/div[1]/div[6]/div/div/div/div/ul/li[2]/a")
    action_click(driver,loginTab)
    continueWithEmail=explicit_wait_xpath(driver,"/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/div/button[3]")
    action_click(driver,continueWithEmail)
    emailField = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/div/form/div[1]/div/input")
    emailField.click()
    emailField.send_keys(email)
    #prevent ghosting
    time.sleep(1)
    passwordField = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/div/form/div[2]/div/input")
    passwordField.send_keys(password)
    submitButton=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/div/form/button").click()
    #check if referral tab is loaded TODO better tests incoming
    referraltab = explicit_wait_presence_xpath(driver,"/html/body/div/main/div/div[3]/div[3]/p")
    time.sleep(3)
    assert driver.current_url in FeedUrlVariations



def Payment(driver):
    driver.get("https://herocircle.app/circle/eu-viable-world-for-all-circle/members")
    PaymentButton=explicit_wait_xpath(driver,"/html/body/div[1]/main/div/article/div[2]/div[1]/div[2]/div/button")
    PaymentButton.click()
    #TODO support for amount of Payment and specific circle
    NextButton=explicit_wait_xpath(driver,"/html/body/div[1]/div[4]/div/div/div/div[3]/button")
    NextButton.click()
    GlobalCircle=explicit_wait_xpath(driver,"/html/body/div[1]/div[4]/div/div/div/div[1]/div[1]/input")
    GlobalCircle.click()
    #Stability on languagues
    NextButton=explicit_wait_xpath(driver,"/html/body/div[1]/div[4]/div/div/div/div[2]/button")
    NextButton.click()
    time.sleep(5)
    #for further testing just temporairly check if it is stripe url
    print(driver.current_url)
    time.sleep(100)
   


def Logout(driver):
    driver.get("https://herocircle.app/feeds/circles2")
    navigationTab=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[3]/div/button")
    time.sleep(0.5)
    navigationTab.click()
    time.sleep(0.5)
    logoutButton=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[2]/div[2]/form/button")
    time.sleep(0.5)
    logoutButton.click()

def change_languague(lang):
    Select(WebDriverWait(driver, default_wait_time).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/nav/div[3]/div/label/select")))).select_by_value(lang)

def start_driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()   
    return driver 
def start_driver_edge():
    driver = webdriver.Edge()
    driver.maximize_window()   
    return driver 
def start_driver_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()   
    return driver 

#TODO
def check_feed():
    #circulate through tabs and get random victory update
    return 0
#TO complete images
def post_victory(driver,title_text,summary_text,body_text):
    HamburgerMenu=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[3]/div/button")
    HamburgerMenu.click()
    Mobilizer_Profile=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[2]/div[2]/form/button")
    Mobilizer_Profile.click()
    Title=explicit_wait_xpath(driver,"/html/body/div[1]/main/div/div[3]/div/div/div/div[1]/div[3]/div/input")
    Title.send_keys(title_text)
    Summary=explicit_wait_xpath(driver,"/html/body/div[1]/main/div/div[3]/div/div/div/div[1]/div[4]/div/input")
    Summary.send_keys(summary_text)
    Body=explicit_wait_xpath(driver,"/html/body/div[1]/main/div/div[3]/div/div/div/div[1]/div[5]/textarea")
    Body.send_keys(body_text)





#driver = start_driver_chrome()
#Login(driver,"khemissimoetez@gmail.com","Hero@123")
#Register_basic(driver,"moetez","khemissi","khemissimoetez15315@gmail.com","+21655602457","Hero@123")
#Login(driver,"khemissimoetez@gmail.com","Hero@123")
#change_languague(Languague["NL"])
#Payment(driver)
#Logout(driver)

#Register_basic(driver,"moetez","khemissi","khemissimoetez@gmail.com","+21655602457","Hero@123")
