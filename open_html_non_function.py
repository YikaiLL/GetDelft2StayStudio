from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import os
import time
# http://www.hongkiat.com/blog/automate-create-login-bot-python-selenium/



room__name = input('Enter Your Room Name: ')
# INPUT room name like "2Z 18", using space as spearate, the first part is the floor num, the second is the room number.

if room__name =='':
    try:
        with open('house_list.json') as data_file:
            house_list_from_file= json.load(data_file)
        print('Dict Length: ',len(house_list_from_file))
        for key in house_list_from_file:
            room__name=key
    except:
        room__name='a b'
        pass

if room__name!='':
    print('Hello ', room__name)
    
    # Input your own account name
    usernameStr = ' @gmail.com'
    # Input your own password
    passwordStr = ' '
    # Input your birth date: DD-MM-YYYY
    birthdayStr='20-03-1999'
    
    # Open login page
    browser = webdriver.Chrome()
    browser.get(('https://delft2stay.nl/customer/account/login/'))

    # input email and password in the page
    username = browser.find_element_by_xpath('//*[@id="email"]')
    username.send_keys(usernameStr)
    password=browser.find_element_by_xpath('//*[@id="pass"]')
    password.send_keys(passwordStr)
    sendButton = browser.find_element_by_xpath('//*[@id="send2"]')
    sendButton.click()

    room_name_list=room__name.lower().split(' ')

    browser.get('https://delft2stay.nl/book-apartment/'+room_name_list[0]+'-'+room_name_list[1]+'.html')

    delay = 3 # seconds
    try:    
# element = WebDriverWait(driver, 6000).until(EC.presence_of_element_located((By.XPATH, qID_xpath_start+str(qIDindex)+qID_xpath_end)))
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="date_of_birth"]')))
        print( "Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

    birthday=browser.find_element_by_xpath('//*[@id="date_of_birth"]')
    birthday.send_keys(birthdayStr)
    # We are foriengerss :)
    foreign_select=browser.find_element_by_xpath('//*[@id="foreign"]')
    foreign_select.click()
    # Find the nearest date that is available. 
    start_date_select=Select(browser.find_element_by_xpath('//*[@id="start_date"]'))
    start_date_select.select_by_index(1);
    
    # Upload the passport 
    passport=browser.find_element_by_xpath('//*[@id="passport"]')
    # File name can be modified according to your passport name and extension
    passport.send_keys(os.getcwd()+"/passport.pdf")
    
    # I am not going to click the book button for you.
    book_button=browser.find_element_by_xpath('//*[@id="product_addtocart_form"]/div[7]/div[2]/div[2]/button')
    
    # Sleep forever
    time.sleep(9999999)
    # return
    
    # Uncomment this if you want to book by script.
    # book_button.click()
    
    # Unccoment the following to accept the terms, I am not going to do that for you.
    # delay = 3 # seconds
    # try:
    #     # element = WeabDriverWait(driver, 6000).until(EC.presence_of_element_located((By.XPATH, qID_xpath_start+str(qIDindex)+qID_xpath_end)))
    #     WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,'//*[@id="checkout-review-submit"]/p[1]/input')))
    #     print( "Page is ready!")
    # except TimeoutException:
    #     print ("Loading took too much time!")
    
    # # webdriver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
    # accept_term=browser.find_element_by_xpath('//*[@id="checkout-review-submit"]/p[1]/input')
    # accept_term.click() 

