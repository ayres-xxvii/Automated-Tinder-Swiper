

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from secret import email, password


class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

    def login(self):
        self.driver.get('https://tinder.com')

        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type = 'button' and @aria-label = 'Log in with Facebook']//span"))).click()

        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
        email_input.send_keys(email)
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_name("login")
        login_btn.click()

        self.driver.switch_to_window(base_window)
        popup_1 = self.driver.find_element_by_id('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        popup_2 = self.driver.find_element_by_id('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        pass


    def dislike(self):
        pass


bot = TinderBot()
bot.login()

