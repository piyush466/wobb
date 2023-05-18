import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Login:
    email_x = '//*[@id="root"]/div[1]/div/div/div/div/div/form/div[1]/div/div[1]/div[1]/input'
    Next_btn_x = "//button[text()='Next']"
    password_name = "password"
    sign_up_x = "//button[text()='Sign In']"
    Campaign_Name = "Name"
    drop_down = "(//div[@class='form-group row']/div/div/div)[2]"
    Deliverables = "//ul[@class='MuiList-root MuiList-dense']/div/div[2]"



    def __init__(self,driver):
        self.driver =driver

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.email_x).send_keys(email)

    def clickNext(self):
        self.driver.find_element(By.XPATH, self.Next_btn_x).click()

    def setpassword(self,password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def clicksign_up(self):
        self.driver.find_element(By.XPATH, self.sign_up_x).click()

    def hover(self):
        action = ActionChains(self.driver)
        self.path = self.driver.find_element(By.XPATH, "(//div[@class='relative h-fit w-fit'])[1]")
        action.move_to_element(self.path).perform()
        time.sleep(3)
        self.post = self.driver.find_element(By.XPATH, "//h5[text()='Post Campaign']")
        action.move_to_element(self.post).click().perform()
        time.sleep(5)

    def Set_Campaign_Name(self,campaign):
        self.driver.find_element(By.NAME, self.Campaign_Name).send_keys(campaign)

    def dropdown_platfrom(self):
        self.driver.find_element(By.CSS_SELECTOR, "#mui-component-select-Platform").click()
        self.apps = self.driver.find_elements(By.XPATH, "//ul[@class='MuiList-root MuiMenu-list MuiList-padding']/li")
        for app in self.apps:
            print(app.text)
            if app.text == "Twitter":
                app.click()
        time.sleep(5)


    def all_drop_down(self):
        time.sleep(2)
        self.drop = self.driver.find_element(By.XPATH, self.drop_down)
        self.drop.click()

    def select_2nd_droplist(self):
        self.second  = self.driver.find_elements(By.XPATH, self.Deliverables)
        for se in self.second:
            print(se.text)
            if se.text == 'Text Tweet':
                self.plus = self.driver.find_element(By.XPATH, "//ul[@class='MuiList-root MuiList-dense']/div/div/div/button[2]")
                self.plus.click()
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div/div/div").click()
        time.sleep(4)
            # if se.text ==





        # // ul[ @class ='MuiList-root MuiMenu-list MuiList-padding'] /li