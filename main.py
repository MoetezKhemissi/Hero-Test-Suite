
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
from selenium.webdriver.chrome.options import Options
from config import default_wait_time
from data import Languague,FeedUrlVariations,BaseProdUrl,BaseStagingUrl
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import re
import os
import string
import random


#------------------------Helpers-----------------------------------
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
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
    
    rdm_string=get_random_string(6)
    #TODO ASAP need to change email until request to delete old
    email="khemissimoetez"+rdm_string+"@gmail.com"
    phone="+21655602457"
    password="Hero@123"
    if os.getenv('TEST_ENV_TARGET')=="staging":
        driver.get(BaseStagingUrl)
    else:
        driver.get(BaseProdUrl)
    accept_cookie(driver)
    joinButton=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[3]/div/button")
    joinButton.click()
    try:
        continueWithEmail=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[7]/div/div/div/div/div/div[1]/div/button[3]")))

    except Exception as e :
        print("stil unstable ..")
    try:
        continueWithEmail=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[6]/div/div/div/div/div/div[1]/div/button[3]")))
    except Exception as e :
        print("stil unstable ..")



    continueWithEmail.click()

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
    agreeTOS= explicit_wait_presence_xpath(driver,"//input[@id='agreeToTOS']")
    agreeTOS.click()
    confirmRegistration=explicit_wait_xpath(driver,"//button[@type='submit']")
    confirmRegistration.click()
    #check if referral tab is loaded TODO better tests incoming
    referraltab = explicit_wait_presence_xpath(driver,"/html/body/div/main/div/div[3]/div[3]/p")
    time.sleep(3)
    assert driver.current_url in FeedUrlVariations


def accept_cookie(driver):
    try:
        AcceptCookie=explicit_wait_xpath(driver,"/html/body/div/section/div/button[1]")
        time.sleep(1)
        AcceptCookie.click()
    except Exception as e:
        print("Cookie Already accepted")
def Login(driver):
    email="khemissimoetez@gmail.com"
    password="Hero@123"
    if os.getenv('TEST_ENV_TARGET')=="staging":
        driver.get(BaseStagingUrl)
    else:
        driver.get(BaseProdUrl)
    accept_cookie(driver)

    joinButton=explicit_wait_xpath(driver,"/html/body/div[1]/nav/div[3]/div/button")
    time.sleep(1)
    joinButton.click()
    time.sleep(1)

    loginTab = WebDriverWait(driver, default_wait_time).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"#tabs-Login")]')))
    loginTab.click()
    time.sleep(2)


    try:
        continueWithEmail=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/div/button[3]")))
    except Exception as e:
        print("Unstable frontend")
    try:
        continueWithEmail=WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[7]/div/div/div/div/div/div[2]/div/button[3]")))
    except Exception as e:
        print("Unstable frontend")
    time.sleep(1)
    continueWithEmail.click()
    emailField = explicit_wait_presence_xpath(driver,"//input[@id='email']")
    emailField.click()
    emailField.send_keys(email)
    #prevent ghosting
    time.sleep(1)
    passwordField = explicit_wait_presence_xpath(driver,"//input[@id='password']")
    passwordField.send_keys(password)
    try:
        submitButton=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/div/form/button").click()
    except Exception as e :
        print("to be improved ..")
    try:
        submitButton=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div/div/div/div[2]/div/form/button").click()
    except Exception as e :
        print("to be improved ..")

        
    #check if referral tab is loaded TODO better tests incoming


def test_login():
    driver=start_driver_chrome()
    Login(driver)
    referraltab = explicit_wait_presence_xpath(driver,"/html/body/div/main/div/div[3]/div[3]/p")
    time.sleep(3)
    assert driver.current_url in FeedUrlVariations


def test_Payment():
    driver=start_driver_chrome()
    Login(driver)
    time.sleep(5)
    if os.getenv('TEST_ENV_TARGET')=="staging":
        driver.get(BaseStagingUrl+"circle/eu-viable-world-for-all-circle/members")
    else:
        driver.get(BaseProdUrl+"circle/eu-viable-world-for-all-circle/members")
    PaymentButton=explicit_wait_xpath(driver,"/html/body/div[1]/main/div/article/div[2]/div[1]/div[2]/div/button")
    time.sleep(0.5)
    PaymentButton.click()
    time.sleep(0.5)
    #TODO support for amount of Payment and specific circle
    NextButton=explicit_wait_xpath(driver,"/html/body/div[1]/div[4]/div/div/div/div[3]/button")
    time.sleep(0.5)
    NextButton.click()
    time.sleep(0.5)
    GlobalCircle=explicit_wait_xpath(driver,"/html/body/div[1]/div[4]/div/div/div/div[1]/div[1]/input")
    time.sleep(0.5)
    GlobalCircle.click()
    time.sleep(0.5)
    #Stability on languagues
    NextButton=explicit_wait_xpath(driver,"/html/body/div[1]/div[4]/div/div/div/div[2]/button")
    time.sleep(0.5)
    NextButton.click()
    time.sleep(5)
    #for further testing just temporairly check if it is stripe url
    assert bool(re.search("https:\/\/checkout\.stripe\.com(.)*", driver.current_url))

   


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
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
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
