from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

gen = random.randint(1, 3)
year = random.randint(1900, 2100) - 1899
month = random.randint(1, 12)
day = random.randint(1, 7)
week = random.randint(1, 6)
hob = random.randint(1, 3)
class SeacrhLocators:
    LOCATOR_FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    LOCATOR_LAST_NAME = (By.ID, 'lastName')
    LOCATOR_EMAIL = (By.CSS_SELECTOR, '#userEmail')
    LOCATOR_GENDER = (By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[' + str(gen)+ ']/label')
    LOCATOR_NUMBER = (By.ID, 'userNumber')
    LOCATOR_DATE_OF_BIRTH = (By.ID, 'dateOfBirthInput')
    LOCATOR_YEAR_OF_BIRTH = (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[' + str(year) + ']')
    LOCATOR_MONTH_OF_BIRTH = (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[' + str(month) + ']')
    LOCATOR_DAY_OF_BIRTH = (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[' + str(week) + ']/div[' + str(day) + ']')
    LOCATOR_SUBJECTS = (By.ID, 'subjectsInput')
    LOCATOR_HOBBY = (By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[' + str(hob) + ']/label')
    LOCATOR_PICTURE = (By.ID, 'uploadPicture')
    LOCATOR_ADDRESS = (By.ID, 'currentAddress')
    LOCATOR_STATE = (By.XPATH, '//*[@id="state"]/div/div[1]')
    LOCATOR_CHOOSE_STATE = (By.XPATH, '//*[@id="state"]/div[2]/div[1]')
    LOCATOR_CITY = (By.XPATH, '//*[@id="city"]/div/div[1]')
    LOCATOR_CHOOSE_CITY = (By.XPATH, '//*[@id="city"]/div[2]/div[1]')
    LOCATOR_SUBMIT = (By.XPATH, '//*[@id="submit"]')

class SearchHelper(BasePage):

    def first_name(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_FIRST_NAME)
        text.send_keys(word)
        return text

    def last_name(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_LAST_NAME)
        text.send_keys(word)
        return text

    def email(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_EMAIL)
        text.send_keys(word)
        return text

    def gender(self):
        return self.find_element(SeacrhLocators.LOCATOR_GENDER).click()

    def number(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_NUMBER)
        text.send_keys(word)
        return text

    def date_of_birth(self):
        return self.find_element(SeacrhLocators.LOCATOR_DATE_OF_BIRTH).click()

    def year_of_birth(self):
        return self.find_element(SeacrhLocators.LOCATOR_YEAR_OF_BIRTH).click()
    
    def month_of_birth(self):
        return self.find_element(SeacrhLocators.LOCATOR_MONTH_OF_BIRTH).click()

    def day_of_birth(self):
        return self.find_element(SeacrhLocators.LOCATOR_DAY_OF_BIRTH).click()

    def subjects(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_SUBJECTS)
        text.send_keys(word)
        text.send_keys(Keys.ENTER)
        return text

    def hobby(self):
        return self.find_element(SeacrhLocators.LOCATOR_HOBBY).click()

    def picture(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_PICTURE)
        text.send_keys(word)
        return text

    def address(self, word):
        text = self.find_element(SeacrhLocators.LOCATOR_ADDRESS)
        text.send_keys(word)
        return text

    def state_1(self):
        return self.find_element(SeacrhLocators.LOCATOR_STATE).click()
    def state_2(self):
        return self.find_element(SeacrhLocators.LOCATOR_CHOOSE_STATE).click()

    def city_1(self):
        return self.find_element(SeacrhLocators.LOCATOR_CITY).click()
    def city_2(self):
        return self.find_element(SeacrhLocators.LOCATOR_CHOOSE_CITY).click()

    def submit(self):
        return self.find_element(SeacrhLocators.LOCATOR_SUBMIT).send_keys(Keys.ENTER)
