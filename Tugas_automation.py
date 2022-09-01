import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_register():
    s = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')

    driver = webdriver.Edge(service=s)
    driver.get("https://barru.pythonanywhere.com/daftar")

    #find button SignUp 
    signIn = driver.find_element(By.ID, 'signUp')
    signIn.click()

    # find name and send keys
    email = driver.find_element(By.ID, 'name_register')
    email.send_keys('tester')

    # find email and send keys
    password = driver.find_element(By.ID, 'email_register')
    password.send_keys('tester@jagoqa.com')

    # find password and send keys
    password = driver.find_element(By.ID, 'password_register')
    password.send_keys('testerjago')

    # find button sign in
    signUp = driver.find_element(By.ID, 'signup_register')
    signUp.click()

    time.sleep(3)
    driver.quit()


def test_login():
    s = Service('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')

    driver = webdriver.Edge(service=s)
    driver.get("https://barru.pythonanywhere.com/daftar")

    # find email and send keys
    email = driver.find_element(By.ID, 'email')
    email.send_keys('tester@jagoqa.com')

    # find password and send keys
    password = driver.find_element(By.ID, 'password')
    password.send_keys('testerjago')

    # find button sign in
    signIn = driver.find_element(By.ID, 'signin_login')
    signIn.click()

    time.sleep(3)

    driver.quit()

test_register()
test_login()