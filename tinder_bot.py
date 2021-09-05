

from selenium import webdriver
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

        time.sleep(8)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        popup_2 = self.driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):

        like_btn = bot.driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = bot.driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
        dislike_btn.click()


    def close_popup(self):
        home_popup = bot.driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div[2]/button[2]')
        home_popup.click()

        
    def close_match(self):
        match_popup = bot.driver.find_element_by_xpath('//*[@id="q-1690254490"]/div/div/div[1]/div/div[4]/button')
        match_popup.click()

    def auto_swipe(self):
        print("ready...")
        while True:
            time.sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()


bot = TinderBot()
bot.login()
