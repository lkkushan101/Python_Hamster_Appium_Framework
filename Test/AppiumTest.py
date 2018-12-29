import os
import unittest
from time import sleep
from appium import webdriver
from Pages.Login import Login
from Pages.MainScreen import MainScreen
from Pages.MakePayment import MakePayment
import allure
import json
import pytest
class ContactAppTestAppium(unittest.TestCase):

    @allure.story('Test Automation Solution - Kushan Amarasiri')
    @allure.feature('Test - Auomation Framework in Python')
    @allure.testcase("Registration Test Case")

    def setUp(self):
        with open('./Data/data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        with pytest.allure.step("Launch site"):
            desired_caps = {}
            desired_caps['platformName'] = data['platformName']

            desired_caps['deviceName'] = data['deviceName']
            desired_caps['appPackage'] = data['appPackage']
            desired_caps['appActivity'] = data['appActivity']

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    def tearDown(self):

        self.driver.quit()


    def test_single_bankapp(self):
        with open('./Data/data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
       # driver = self.driver
        login = Login(self.driver)
        login.setUserName(data['User'])
        login.setPassword(data['User'])
        login.clickLogin()

        mainScreen = MainScreen(self.driver)
        mainScreen.clickMakePayment()
        makePaymentScreen = MakePayment(self.driver)
        makePaymentScreen.makePayment(data['tele'],data['name'],data['country'])
        sleep(5)


