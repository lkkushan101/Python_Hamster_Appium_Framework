from behave import given, when, then
from time import sleep
from appium import webdriver
from Pages.Login import Login
from Pages.MainScreen import MainScreen
from Pages.MakePayment import MakePayment
import allure
import json

with open('./Data/data.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']

    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


@given(u'I logged into the bank Application')
def step_impl(context):
    with open('./Data/data.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        # driver = self.driver
    login = Login(driver)
    login.setUserName(data['User'])
    login.setPassword(data['User'])
    login.clickLogin()

@when(u'I make payment with the app')
def step_impl(context):
    with open('./Data/data.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        # driver = self.driver


    mainScreen = MainScreen(driver)
    mainScreen.clickMakePayment()
    makePaymentScreen = MakePayment(driver)
    makePaymentScreen.makePayment(data['tele'], data['name'], data['country'])
    sleep(5)


@then(u'App should accept the payment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then App should accept the payment')

